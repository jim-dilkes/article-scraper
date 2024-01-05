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

import datetime
args = (Q(name='BBC News'),)
filter_kwargs = {
        'scraper' + '__status': 'A',
        'scraper_runtime' + '__next_action_time__lt': datetime.datetime.now(),
    }

ref_obj_list = NewsWebsite.objects.filter(*args)#, **filter_kwargs)

print(f"ARGS:\n{args}")
print(f"KWARGS:\n{filter_kwargs}")
print(ref_obj_list.values())



for ref_object in ref_obj_list:
    print(ref_object.scraper_runtime)
    print(ref_object.scraper_runtime.next_action_time)
    print(datetime.datetime.now())
    print(ref_object.id)
    print(ref_object.pk)


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



# import urllib.request, urllib.parse, http.client
# param_dict = {
#             'project': 'default',
#             'spider': 'article_spider',
#             'id': 1,
#             'run_type': 'TASK',
#             'do_action': 'yes'
#         }
# hostname = 'localhost'
# #hostname = '192.168.99.100'
# port='6800'

# params = urllib.parse.urlencode(param_dict)
# headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# print("3")
# conn = http.client.HTTPConnection(f"{hostname}:{port}")
# print("4")
# conn.request("POST", "/schedule.json", params, headers)
# print("5")
# response = conn.getresponse()
# print(response.status)
# print(response.reason)
# print(response.msg)
# print(response.read())