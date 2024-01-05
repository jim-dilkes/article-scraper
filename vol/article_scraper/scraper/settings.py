import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "article_insight_generator.settings") #Changed in DDS v.0.3

BOT_NAME = 'article_scraper'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'article_scraper.scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

#Scrapy 0.20+
ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'article_scraper.scraper.pipelines.DjangoWriterPipeline': 800,
}

DSCRAPER_CUSTOM_PROCESSORS = [
    'article_scraper.scraper.processors'
]

# #Scrapy up to 0.18
# ITEM_PIPELINES = [
#     'dynamic_scraper.pipelines.ValidationPipeline',
#     'article_scraper.scraper.pipelines.DjangoWriterPipeline',
# ]