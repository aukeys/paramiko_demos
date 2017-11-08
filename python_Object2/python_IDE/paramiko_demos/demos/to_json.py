#!/usr/bin/python
#-*- conding: UTF-8 -*-
import json
import mysql_helper
import re
def To_Json():
    mysql = mysql_helper.MySQLHelper()
    domain_info = mysql.select_All('select status,net_ip,domain,domain_id,id from domain')
    if len(domain_info) > 0:
        # for k in domain_info[0]:
        #     print "| %s  \t"%(k),
        # for hostz in range(len(domain_info)):
        #     # print a[hostz]
        #     print ""
        #     for k,v in domain_info[hostz].items():
        #         print "| %s  \t"%(v),
        # print "|"
        return domain_info

    else:
        return "No slect doamin info,please check domain table.."
#
# def Re_Echo(hostname):
#     return_list=[]
#     re_hostname = re.escape(hostname)
#     domain_info = To_Json()
#     # print domain_info
#     print len(domain_info)
#     for i in range(len(domain_info)):
#         for k,v in  domain_info[i].items():
#             print re.findall(".*"+re_hostname+".*", v.encode("utf-8"))
#             # if re.findall(".*"+re_hostname+".*", v):
#             if re.findall(".*"+re_hostname+".*", v.encode("utf-8")):
#                 return_list2=return_list.append(domain_info[i])
#                 #return domain_info[i]
#                 print "domain_info[i]",domain_info[i]
#                 print type(domain_info[i])
#                 a=domain_info[i]
#                 az=return_list.append(a)
#                 print a
#                 print "az",az
#                 print "return_list2---",return_list.append(domain_info[i])
#                 # break;
#             # else:
#             #     return "ERRORERROR"
#             print "AAAA"
# #print To_Json()
# print Re_Echo('192.168.96.2')