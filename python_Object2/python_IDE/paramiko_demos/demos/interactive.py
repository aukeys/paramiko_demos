#!/usr/bin/python
# -*- coding: UTF-8 -*-
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
#2017

import socket
import sys
from paramiko.py3compat import u
import time,os
# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan,username,hostname):
    if has_termios:
        print "posix_shell"
        posix_shell(chan,username,hostname)

    else:
        print "windows_shell"
        windows_shell(chan)



def posix_shell(chan,username,hostname):
    import select
    print "username",username
    oldtty = termios.tcgetattr(sys.stdin)
    f = file('record.txt','ab+')
    import mysql_helper
    conn = mysql_helper.MySQLHelper()
# domain_id2=11
# a= mysql.select_One('select * from domain where domain_id=%s',domain_id2)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        records = []
        #users = os.getlogin()
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    sys.stdout.write(x)
                    #print "chenrui"
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                records.append(x)
                if x == '\r':
                    # print 'your input:',''.join(records)
                    # print "_____________",records
                    # c_time = time.strftime('%Y-%M-%d %H:%m:%S')
                    c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                #    cmd = ''.join(records).replace('\r','\n')
                #     cmd = ''.join(records).replace('\r','\n')
                    cmd = ''.join(records).replace('\r',"")
                    # cmd = ''.join(cmd).replace('\t'," ")
                    log = '%s  %s  %s\n'%(c_time,username,cmd)
                    # print len(cmd)
                    # print "CMD:::",cmd
                    # print len(cmd)
                    if  0 < len(cmd) < 2:# or len(cmd) != 1:
                        f.write(log)
                        #print mysqlhelp.select_One('select * from t2 where id > %s',1)
                        #conn.select_One()
                        #a=(c_time,username,cmd,hostname)
                        a=(username,str(cmd),hostname,'','client_IP',c_time,'client_time')
                        print "a___",str(cmd)

                        conn.insert_One('insert into record(user,command,net_ip,unet_ip,log_ip,time,net_time) values(%s,%s,%s,%s,%s,%s,%s)',a)
                        # if cmd == "exit":
                        #     print "lllllllllllllll大l"

                        records = []
                    elif len(cmd) == 0:
                        cmd = ''.join(records).replace('\r',"==Enter==")
                        # cmd = cmd.replace('\r',"==Enter==")
                        log = '%s  %s  %s\n'%(c_time,username,cmd)
                        f.write(log)
                        # print "len(cmd)",cmd
                        a=(username,str(cmd),hostname,'','client_IP',c_time,'client_time')
                        # print cmd
                        conn.insert_One('insert into record(user,command,net_ip,unet_ip,log_ip,time,net_time) values(%s,%s,%s,%s,%s,%s,%s)',a)
                        records = []
                    else:
                       # pass
                       # print "kong kong "
                       # cmd = cmd.replace('\n',"==Enter==\n")
                       # log = '%s  %s  %s\n'%(c_time,username,cmd)
                       f.write(log)
                       # a=(username,cmd,hostname,'','client_IP',c_time,'client_time')
                       # if str(cmd) == "logout":
                       #     cmd = "logout"
                       a=(username,str(cmd),hostname,'','client_IP',c_time,'client_time')
                       conn.insert_One('insert into record(user,command,net_ip,unet_ip,log_ip,time,net_time) values(%s,%s,%s,%s,%s,%s,%s)',a)
                       records = []
                #print "x:",x
                if len(x) == 0:
                    break
                chan.send(x)
        #print "chenrui:",records
        conn.closeConn()

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
        f.close()
    
# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
        
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()
        
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
        
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass
