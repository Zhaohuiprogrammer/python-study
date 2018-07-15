#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-15 15:25:01
# @Author  : zhulei (zhuleimailname@gmail.com)
# @Link    : http://zhuleiblog.com

from urllib import request


class HtmlDownloader(object):
    """Html下载器"""
    def download(self, url):
        if url is None:
            return None

        response = request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()