# vim: set fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4 softtabstop=4 :

import re
import os

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from wikiextract.items import WikiItem

class TracwikiSpider(CrawlSpider):
    domain_name = 'localhost'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost/trac/main/wiki/WikiStart']
    http_user = ''
    http_pass = ''

    def __init__(self):
        creds = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'password.txt')).readline()
        self.http_user, self.http_pass = creds.split(',', 1)
        super(CrawlSpider, self).__init__()

    def parse(self, response):
        xs = HtmlXPathSelector(response)
        
        links = xs.select('//div[@id="content"]//a/@href').extract()
        for link in links:
            yield Request('http://localhost' + link, callback=self.parse)
        
        breadcrumb = xs.select('//div[@id="content"]/p[1]').extract()
        content = xs.select('//div[@id="content"]/div[1]').extract()

        if isinstance(content, list):
            content = u''.join(content)
        
        content = content.replace(u'"/trac/main/wiki/', u'"/docs/')

        if breadcrumb:
            if isinstance(breadcrumb, list):
                breadcrumb = u''.join(breadcrumb)

            breacrumb = breadcrumb.replace(u'"/trac/main/wiki/', u'"/docs/')
            content = u'<div class="wikipage">{0}{1}</div>'.format(breadcrumb, content)
        
            content = content.replace(u'<br style="clear: both">', u'<br style="clear: both" />')

        # Fuck that.
        content = ''.join([x for x in content if ord(x) in range(128)])

        yield WikiItem(url=response.url, content=content)

SPIDER = TracwikiSpider()
