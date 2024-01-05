from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem


class NewsWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return f"{self.name} - {self.scraper.name}"


class Article(models.Model):
    title = models.CharField(max_length=256)
    news_website = models.ForeignKey(NewsWebsite)
    description = models.TextField(blank=True)
    article_content = models.TextField(blank=True)
    time_published = models.PositiveIntegerField(null=True)
    url = models.URLField()
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return (f"{self.news_website.name} - {self.title}")



class ArticleItem(DjangoItem):
    django_model = Article
