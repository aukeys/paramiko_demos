#!/usr/bin/python
#-*- coding: UTF-8 -*-
#!/usr/bin/env python
  
import requests
import csv
  
def getIp(file):
  iplist = []
  fi = open(file, 'r')
  for ip in fi:
    ip = ip.strip()
    iplist.append(ip)
  return iplist
  
def get_geolocation(ip):
  r = requests.get('https://freegeoip.net/json/' + ip)
  info = [str(r.json()['country_name']), str(r.json()['city'])]
  return {'ip':ip, 'country_name':info[0], 'city_name':info[1]}
  
if __name__ == '__main__':
  iplist = getIp('/root/ipfile')
  f = open('outputinfo.csv', 'a+')
  fieldnames = ['ip', 'country_name', 'city_name']
  dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
  dict_writer.writerow(dict(zip(fieldnames, fieldnames)))
  for ip in iplist:
    data = get_geolocation(ip)
    dict_writer.writerow(data)
