# coding:utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')

import django
django.setup()

from subject.models import Subject, Page


def testscript():
    python_cat = add_cat('Python')  # 创建python目录类
    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")
    add_page(cat=python_cat,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/")
    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/")
    django_cat = add_cat("Django")  # 创建Django目录类
    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    add_page(cat=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/")
    add_page(cat=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/")
    frame_cat = add_cat("Other Frameworks")
    add_page(cat=frame_cat,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/")
    add_page(cat=frame_cat,
             title="Flask",
             url="http://flask.pocoo.org")
    # Print out what we have added to the user.
    for c in Subject.objects.all():
        for p in Page.objects.filter(Subject=c):
            print "­ {0} ­ {1}".format(str(c), str(p))
# 函数定义


def add_page(cat, title, url, view=0):
    p = Page.objects.get_or_create(
        Subject=cat, title=title, url=url, view=view)[0]
    return p


def add_cat(name):
    c = Subject.objects.get_or_create(name=name)[0]
    return c
# 从这里开始执行!
if __name__ == '__main__':
    print "Starting itcastsubject population script..."
    testscript()
