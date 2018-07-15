#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-15 15:25:31
# @Author  : zhulei (zhuleimailname@gmail.com)
# @Link    : http://zhuleiblog.com
import re
from urllib import parse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # <a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        # <h2>（计算机程序设计语言）</h2>
        # <a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
        # <a class="lock-lemma" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
        # </dd>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        # <div class="para" label-module="para">Python<sup class="sup--normal" data-sup="1">
        # [1]</sup><a class="sup-anchor" name="ref_[1]_21087">&nbsp;</a>
        # （英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型<a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>，由荷兰人<a target="_blank" href="/item/Guido%20van%20Rossum">Guido van Rossum</a>于1989年发明，第一个公开发行版发行于1991年。</div><div class="para" label-module="para">Python是纯粹的<a target="_blank" href="/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6/405190" data-lemmaid="405190">自由软件</a>， <a target="_blank" href="/item/%E6%BA%90%E4%BB%A3%E7%A0%81/3969" data-lemmaid="3969">源代码</a>和<a target="_blank" href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8">解释器</a>CPython遵循 <a target="_blank" href="/item/GPL">GPL</a>(<a target="_blank" href="/item/GNU">GNU</a> General Public License)协议。Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。</div><div class="para" label-module="para">Python具有丰富和强大的库。它常被昵称为<a target="_blank" href="/item/%E8%83%B6%E6%B0%B4%E8%AF%AD%E8%A8%80/3564482" data-lemmaid="3564482">胶水语言</a>，能够把用其他语言制作的各种模块（尤其是<a target="_blank" href="/item/C/7252092" data-lemmaid="7252092">C</a>/<a target="_blank" href="/item/C%2B%2B">C++</a>）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，用更合适的语言改写，比如<a target="_blank" href="/item/3D%E6%B8%B8%E6%88%8F">3D游戏</a>中的图形渲染模块，性能要求特别高，就可以用<a target="_blank" href="/item/C%2FC%2B%2B/6824246" data-lemmaid="6824246">C/C++</a>重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供<a target="_blank" href="/item/%E8%B7%A8%E5%B9%B3%E5%8F%B0/8558902" data-lemmaid="8558902">跨平台</a>的实现。</div><div class="para" label-module="para">7月20日，<a target="_blank" href="/item/IEEE/150905" data-lemmaid="150905">IEEE</a>发布2017年编程语言排行榜：Python高居首位<sup class="sup--normal" data-sup="2">
        # [2]</sup><a class="sup-anchor" name="ref_[2]_21087">&nbsp;</a>
        # 。</div><div class="para" label-module="para">2018年3月，该语言作者在邮件列表上宣布 Python 2.7将于2020年1月1日终止支持。用户如果想要在这个日期之后继续得到与Python 2.7有关的支持，则需要付费给商业供应商。<sup class="sup--normal" data-sup="3">
        # [3]</sup><a class="sup-anchor" name="ref_[3]_21087">&nbsp;</a>
        # </div>
        # </div>
        summary_node = soup.find('div', class_='lemma-summary').find('div', class_='para')
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
