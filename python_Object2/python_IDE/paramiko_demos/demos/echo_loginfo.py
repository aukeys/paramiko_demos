#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql_helper
import os,sys



path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
files = file("%s/demos/login_domainInfo.sys" % (path),'w+')
table1 =  "|--------------------login domain-----------------------|\n"
table2 = ""
files.write(table1)
files.close()

#info = "|\033[;31;1m   domain_id\t\tdomain\t\t\tstatus\033[0m  |\n"
#print table1
#print info

files = file("%s/demos/login_domainInfo.sys" % (path),'a+')

conn = mysql_helper.MySQLHelper()
select_All = conn.select_All('select * from domain where id >= %s',1)
for lis in xrange(len(conn.select_All('select * from domain where id >= %s',1))):
    #for key,value in select_All[lis].viewitems():
    #    if key == 'domain' or key == 'domain_id' or key == 'status':
    #        print "key=%s,value=%s"%(key,value)
    lists = select_All[lis]
    if lists['status'] == "1":
        #print "%s\t\t%s\t" %(lists['domain_id'],lists['domain']),
        lis = "|   %s\t\t%s\t" %(lists['domain_id'],lists['domain']),
        files.write('%s'%(lis))
    else:
        #print "%s\t\t\033[;31;1m%s\033[0m\t" %(lists['domain_id'],lists['domain']),
        lis = "|   %s\t\t\033[;31;1m%s\t\033[0m" %(lists['domain_id'],lists['domain']),
        files.write('%s'%(lis))

    #print "\t|".rjust(10)
    lis2 = "\t\t|".rjust(16)
    files.write('%s\n'%(lis2))
files.close()




