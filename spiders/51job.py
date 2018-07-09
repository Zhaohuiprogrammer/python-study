#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-09 08:33:46
# @Author  : zhulei (zhuleimailname@gmail.com)
# @Link    : http://zhuleiblog.com

from urllib import request


def get_html(url, code):
    html = None
    try:
        req = request.Request(url)
        resp = request.urlopen(req)
        html = resp.read().decode(code)
    except Exception as e:
        print(e)
    return html


url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

html = get_html(url, 'gbk')
print(html)


