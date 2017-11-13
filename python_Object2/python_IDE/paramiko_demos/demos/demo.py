#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import base64
from binascii import hexlify
import getpass
import os
import select
import socket
import sys
import time
import traceback
from paramiko.py3compat import input
import re
import to_json

import paramiko
try:
    import interactive
except ImportError:
    from . import interactive

import mysql_helper
mysql = mysql_helper.MySQLHelper()

def agent_auth(transport, username):
    """
    Attempt to authenticate to the given transport using any of the private
    keys available from an SSH agent.
    """
    
    agent = paramiko.Agent()
    agent_keys = agent.get_keys()
    if len(agent_keys) == 0:
        return
        
    for key in agent_keys:
        print('Trying ssh-agent key %s' % hexlify(key.get_fingerprint()))
        try:
            transport.auth_publickey(username, key)
            print('... success!')
            return
        except paramiko.SSHException:
            print('... nope.')


def manual_auth(username, hostname):
    default_auth = 'p'
    auth = input('Auth by (p)assword, (r)sa key, or (d)ss key? [%s] ' % default_auth)
    if len(auth) == 0:
        auth = default_auth

    if auth == 'r':
        default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
        path = input('RSA key [%s]: ' % default_path)
        if len(path) == 0:
            path = default_path
        try:
            key = paramiko.RSAKey.from_private_key_file(path)
        except paramiko.PasswordRequiredException:
            password = getpass.getpass('RSA key password: ')
            key = paramiko.RSAKey.from_private_key_file(path, password)
        t.auth_publickey(username, key)
    elif auth == 'd':
        default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_dsa')
        path = input('DSS key [%s]: ' % default_path)
        if len(path) == 0:
            path = default_path
        try:
            key = paramiko.DSSKey.from_private_key_file(path)
        except paramiko.PasswordRequiredException:
            password = getpass.getpass('DSS key password: ')
            key = paramiko.DSSKey.from_private_key_file(path, password)
        t.auth_publickey(username, key)
    else:
        #username = "root"
        # aa=0
        pw = getpass.getpass('Password for %s@%s: ' % (username, hostname))
        # print pw
        # print username
        # print hostname
        if len(pw) <= 0:
            print "请输入密码!!!."
            exit(1)
        else:
             try:
                t.auth_password(username, pw)
             except Exception as e:
                print "密码可能错误，请重试！！！"
                exit(1)





# setup logging
paramiko.util.log_to_file('demo.log')

username = ''
port = ''
if len(sys.argv) > 1:
    hostname = sys.argv[1]
    if hostname.find('@') >= 0:
        username, hostname = hostname.split('@')
        if hostname.find(':') >=0:
            hostname,portstr = hostname.split(':')
            port = int(portstr)
    elif hostname.find(':') >= 0:
            hostname,portstr = hostname.split(':')
            port = int(portstr)
else:
    '''这是把 输入的 domain id 转变成 服务器IP  ssh登录上去'''

    print "\033[30;31;3m====选择登录的服务器====\033[0m"

    #hostname = input('Hostname: ')

    x=0
    while x<5:
        hostname = input('请输入任意信息: ')
        try:
            if len(hostname) == 0:
                print "hostname is not Null."
                exit(1)
            re_hostname = re.escape(hostname)
            domain_info = to_json.To_Json()
            # print "domain_info",domain_info
            # print "re_hostname",re_hostname
            import re
            ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
            if ip.match(hostname):
                print "::::::::",hostname
                break

            else:
                print "ip 不合法.请重新输入."
                ## sys.exit(10)


        except Exception as e:
            import os
            os.system('clear')

        for i in range(len(domain_info)):
            for k,v in  domain_info[i].items():
                # print "re.findall....",re.findall(".*"+re_hostname+".*", str(v))
                # print "hostname",hostname
                if re.findall(".*"+re_hostname+".*", str(v)):
                    print "节点信息:",domain_info[i]
                    break;
        x=x+1
    else:
        print "超过5次....被强制退出"
        exit(1)
    # else:
    #     print "请输入存在的Domain_ID"
    #     exit(1)

# if len(hostname) == 0:
#     print('*** Hostname required.')
#     sys.exit(1)
# port = 22
# if hostname.find(':') >= 0:
#     hostname, portstr = hostname.split(':')
#     port = int(portstr)

#print hostname
# a= mysql.select_One('select net_ip from domain where domain_id=%s'% hostname)
# a= mysql.select_One('select * from domain where domain_id=%s'% hostname)
# a= mysql.select_All('select * from domain where domain_id=%s'% hostname)
# print a[0]
# print a[1]
# hostname = a['net_ip']
# print hostname



if port == '':
    port = 22
if username == '':
    username = 'root'
# import re
# ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
# if ip.match(hostname):
#     print "::::::::",hostname
# else:
#     print "ip 不合法."
#     sys.exit(10)
# now connect
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "\033[31;32;3mLogin: \033[30;31;1m%s %s %s\033[0m\n"%(username,hostname,port)
    # print "hostname,user,port%s%s%s"%(hostname,username,port)
    sock.connect((hostname, port))
except Exception as e:
    print('*** Connect failed: ' + str(e))
    # traceback.print_exc()
    sys.exit(1)
# else:
#     print "重新执行..."


try:
    t = paramiko.Transport(sock)
    try:
        t.start_client()
    except paramiko.SSHException:
        print('*** SSH negotiation failed.')
        sys.exit(1)

    try:
        keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    except IOError:
        try:
            keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
        except IOError:
            print('*** Unable to open host keys file')
            keys = {}

    # check server's host key -- this is important.
    key = t.get_remote_server_key()
    if hostname not in keys:
        print('*** WARNING: Unknown host key!')

    elif key.get_name() not in keys[hostname]:
        print('*** WARNING: Unknown host key!')
##        print "chenrui2S"

    elif keys[hostname][key.get_name()] != key:
        print('*** WARNING: Host key has changed!!!')
        sys.exit(1)
    else:
        print('*** Host key OK.')

    # get username
    if username == '':
        default_username = getpass.getuser()
        username = input('Username [%s]: ' % default_username)
        if len(username) == 0:
            username = default_username

    agent_auth(t, username)
    if not t.is_authenticated():
        manual_auth(username,hostname)
        # print "aaaa"
    if not t.is_authenticated():
        print('*** Authentication failed. :(')
        t.close()
        sys.exit(1)

    chan = t.open_session()
    chan.get_pty()
    chan.invoke_shell()
    print('*** Here we go!\n')
    #print hostname
    interactive.interactive_shell(chan,username,hostname)
    mysql.closeConn()
    chan.close()
    t.close()

except Exception as e:
    print('*** Caught exception: ' + str(e.__class__) + ': ' + str(e))
    traceback.print_exc()
    try:
        t.close()
    except:
        pass

    sys.exit(1)
