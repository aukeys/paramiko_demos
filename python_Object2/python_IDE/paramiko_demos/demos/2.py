#!/usr/bin/python
#-*- coding: UTF-8 -*-
import inet.http;
def getIp():
	http = inet.http()
	http.flags = 0x80000000/*_INTERNET_FLAG_RELOAD强制文件从服务器下载不是缓存*/
      | 0x4000000/*_INTERNET_FLAG_DONT_CACHE*不缓存数据*/
	str = http.get("http://fw.qq.com/ipaddress")
	return str?string.match(str,'"(.+?)"')

io.open()
io.print(getIp())
