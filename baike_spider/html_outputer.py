#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-15 15:26:20
# @Author  : zhulei (zhuleimailname@gmail.com)
# @Link    : http://zhuleiblog.com

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        f_out = None
        try:
            f_out = open('output.html', 'w', encoding='utf-8')

            f_out.write("<html>")
            f_out.write("<body>")
            f_out.write("<table>")

            for data in self.datas:
                f_out.write("<tr>")
                f_out.write("<td style=\"width:500;word-break:break-all\">%s</td>" % data['url'])
                f_out.write("<td style=\"width:150;word-break:break-all\">%s</td>" % data['title'])
                f_out.write("<td>%s</td>" % data['summary'])

            f_out.write("</table>")
            f_out.write("</body>")
            f_out.write("</html>")
        finally:
            if f_out:
                f_out.close()

