#!/usr/bin/python
#-*- coding: UTF-8 -*-
import console;
import web.script
import inet.http;
jsVm = web.script("JavaScript")
jsVm.AddCode( inet.http().get("http://fw.qq.com/ipaddress") )
ipAddr = jsVm.CodeObject.IPData[0];
console.log( "您的外网IP地址:",ipAddr )
