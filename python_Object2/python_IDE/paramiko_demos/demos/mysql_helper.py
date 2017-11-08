#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import os,sys

class MySQLHelper(object):
    '''MySQLHelper 类是用于:
    1. select
    2. insert
    3. delete
    4. update
    5. 其它
    '''
    def __init__(self):
        path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
        mysqlFile = file("%s/demos/mysql.ini" % (path),'r')
        # mysqlFile = file("/python_IDE/python_IDE/paramiko_demos/demos/mysql.ini",'r')
        lis = mysqlFile.readlines()
        self.host = lis[0].strip().split('=')[1]
        self.user = lis[1].strip().split('=')[1]
        self.passwd = lis[2].strip().split('=')[1]
        self.port = lis[3].strip().split('=')[1]
        self.db = lis[4].strip().split('=')[1]
        self.charset = lis[5].strip().split('=')[1]
        #print lis
        mysqlFile.close()
       # print "host:\t %s\nuser:\t %s\npasswd:\t %s\nport:\t %s\ndb:\t %s" % (self.host,self.user,self.passwd,self.port,self.db)
        try:
            self.conn = MySQLdb.connect(host = self.host,user = self.user,passwd = self.passwd,port = int(self.port),db = self.db,charset=self.charset)
            self.cur = self.conn.cursor(cursorclass= MySQLdb.cursors.DictCursor)
        except MySQLdb.Error as e:
            print ("Mysql Error %d: %s"% (e.args[0],e.args[1]))
    def closeConn(self):
        self.conn.close()
        self.cur.close()
       # print "\033[30;32;3mMysql connection is closed...\033[0m"

    def select_One(self,sql,*args):
        #print "查询开始select_One"
        # print "-----",sql
        reCount = self.cur.execute(sql,*args)
        data = self.cur.fetchone()
        return data

    def select_All(self,sql,*args):
        #print "查询开始select_All"
        reCount = self.cur.execute(sql,*args)
        data = self.cur.fetchall()
        # print type(data)
        # print "select_All",data
        return data

    def insert_One(self,sql,*args):
        #print "插入insert_One"
        reCount = self.cur.execute(sql,*args)
        self.conn.commit()

    def delete_One(self,sql,*args):
        reCount = self.cur.execute(sql,*args)
        self.conn.commit()
    def update_One(self,sql,*args):
        reCount = self.cur.execute(sql,*args)
        self.conn.commit()

#mysql = MySQLHelper()
#domain_id2=11
#a= mysql.select_One('select * from domain where domain_id=%s',domain_id2)
#b = mysql.select_One('select domain.domain_id as domainid,record.log_ip as recordlog_ip from record,domain where  domain.domain_id = %s and  record.domain_id = %s ',(domain_id2,domain_id2))
#print "domain Table info:\t %s",a
#print a['net_ip']
#print a['unet_ip']
#print a['log_ip']
#print "domain and record Table info:\t %s", b
#print "login _ client _远程IP:\t %s",b['recordlog_ip']
#print mysqlhelp.select_All('select * from t2 where id > %s',1)

#sqlss = ('chenrui','pppppppppppppppp','10.1.1.17','127.0.0.1','203.86.31.61','2016-35-20 13:12:38','Wed Dec 21 15:38:50 CST 2016')

#mysql.insert_One('insert into record(user,command,net_ip,unet_ip,log_ip,time,net_time) VALUES (%s)',sqlss)

#mysql.insert_One('insert into record(user,command,net_ip,unet_ip,log_ip,time,net_time) values(%s,%s,%s,%s,%s,%s,%s)',sqlss)
#print mysql.select_All('select * from domain where id >= %s',1)
##mysqlhelp.conn.commit()
#mysqlhelp.delete_One('delete from t2 where id > %s',3)
#mysqlhelp.update_One("update t2 set name = 'aaaaaa' where id >= %s",3)

#print mysqlhelp.select_All('select * from t2 where id > %s',1)
#mysqlhelp.closeConn()
#print mysqlhelp.select_One('select name,password from UserTab where name = %s and password = %s ',('chenrui','123'))
#mysql.closeConn()









