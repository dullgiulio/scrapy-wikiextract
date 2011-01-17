# Scrapy settings for wikiextract project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'wikiextract'
BOT_VERSION = '1.0'

LOG_LEVEL = 'WARNING'

SPIDER_MODULES = ['wikiextract.spiders']
NEWSPIDER_MODULE = 'wikiextract.spiders'
DEFAULT_ITEM_CLASS = 'wikiextract.items.WikiItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['wikiextract.pipelines.WikiextractPipeline']

DOWNLOADER_MIDDLEWARES = {
   'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 1,
}

