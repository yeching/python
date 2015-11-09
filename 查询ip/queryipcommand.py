#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import json
import urllib
import sys


def get_data(ip):
    API = "http://ip.taobao.com/service/getIpInfo.php?ip="
    url = API + sys.argv[1]
    jsondata = json.loads(urllib.urlopen(url).read())
    if jsondata['code'] == 1:
        print("No %s info." % ip)
        exit(1)
    else:
        return jsondata

def process_data(jsondata):    
    if jsondata['data']['country']:
        country = jsondata['data']['country']
    else:
        country = "NULL"

    if jsondata['data']['area']:
        area = jsondata['data']['area']
    else:
        area = "NULL"

    if jsondata['data']['region']:
        region = jsondata['data']['region']
    else:
        region = "NULL"

    if jsondata['data']['city']:
        city = jsondata['data']['city']
    else:
        city = "NULL"

    if jsondata['data']['county']:
        county = jsondata['data']['county']
    else:
        county = "NULL"

    if jsondata['data']['isp']:
        isp= jsondata['data']['isp']
    else:
        isp = "NULL"
    return (country, area, region, city, county, isp)

def output_data(data):
    ret = "%-4s\t%-4s\t%-4s\t%-4s\t%-4s\t%-4s\n" % ("country", "area", "region", "city", "county", "isp")
    ret += "%-4s\t%-4s\t%-4s\t%-4s\t%-4s\t%-4s" % data
    print(ret)


#main
def main():
    ret = get_data(sys.argv[1])
    result = process_data(ret)
    output_data(result)

if __name__=='__main__':
    main()
