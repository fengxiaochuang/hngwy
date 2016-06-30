# python
# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hngwy.items import PageItem
import re


class DefaultSpider(CrawlSpider):
    def __init__(self, conf):
        self.conf = conf
        self.name = conf.name
        self.start_urls = conf.url.split(",")
        rule_list = []
        rule_list.append(Rule(LinkExtractor(restrict_xpaths=["//ul[@class='list']/li"]), callback="parse_item"))
        # rule_list.append(Rule(LinkExtractor(restrict_xpaths=["//div[@class='pages']/a[3]"])))
        self.rules = tuple(rule_list)
        super(DefaultSpider, self).__init__()

    def parse_item(self, response):
        page = PageItem()
        try:
            title = response.xpath("//h1/text()").extract_first()
            page["title"] = title
        except Exception:
            page["title"] = ""

        try:
            date = response.xpath("//div[@class='source']/span[2]/text()").re_first(u'201[56]-\d{1,2}-\d{2}')
            page["date"] = date
        except Exception:
            page["date"] = ""

        try:
            content = response.xpath("//div[@id='article_content']").extract_first()
            #content = re.findall(u'id=\"article_content\" style=\"font-size\:14px\;\">\s*(.*)\s*<br>\s*<script', content, re.M)
            content = re.findall(u'id=\"article_content\" style=\"font-size\:14px\;\">\s+(.*)\s+<br>\s+<script', content,
                       re.DOTALL)
            page["content"] = content[0]
        except Exception:
            page["content"] = ""

        page["url"] = response.url
        yield page
