#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-15 15:23:26
# @Author  : zhulei (zhuleimailname@gmail.com)
# @Link    : http://zhuleiblog.com
from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class Spider(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.html_parser = html_parser.HtmlParser()
        self.html_outputer = html_outputer.HtmlOutputer()

    def craw(self, rootUrl):

        count = 1
        self.url_manager.add_new_url(rootUrl)
        while self.url_manager.has_new_url():
            try:

                new_url = self.url_manager.get_new_url()
                print("craw%d -> %s" % (count, new_url))
                content = self.downloader.download(new_url)
                new_urls, data = self.html_parser.parse(new_url, content)
                self.url_manager.add_new_urls(new_urls)
                self.html_outputer.collect_data(data)

                if count == 1000:
                    break
                count = count + 1

            except:
                print('craw failed')

        self.html_outputer.output_html()


root_url = "https://baike.baidu.com/item/Python/407313"

if __name__ == "__main__":
    spider = Spider()
    spider.craw(root_url)