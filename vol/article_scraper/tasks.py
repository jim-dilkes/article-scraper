from celery import shared_task
import os
import sys
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "article_insight_generator.settings"
print("Setting up django")
django.setup()

from celery.task import task
from django.db.models import Q
from dynamic_scraper.utils.task_utils import TaskUtils
from article_scraper.models import NewsWebsite, Article

#sys.path.append("/home/ubuntu/MYPROJECT")
os.environ["DJANGO_SETTINGS_MODULE"] = "article_insight_generator.settings"
django.setup()

@task(name="test_task")
def debug_task():
    print("This is just a test.")
    return "Return this value"


@task()
def run_spiders(prefix=''):
    t = TaskUtils()

    # Q arguments for complex queries
    args = (Q(name__startswith=prefix),)
    t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider')

    return 'COMPLETE'


# @task()
# def run_checkers():
#     t = TaskUtils()
#     #Optional: Django field lookup keyword arguments to specify which reference objects (Article)
#     #to use for checker runs, e.g.:
#     kwargs = {
#         'check_me': True, #imaginary, model Article hat no attribute 'check_me' in example
#     }
#     #Optional as well: For more complex lookups you can pass Q objects vi args argument
#     args = (Q(id__gt=100),)
#     t.run_checkers(Article, 'news_website__scraper', 'checker_runtime', 'article_checker', *args, **kwargs)