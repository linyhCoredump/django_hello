from django.conf.urls import patterns, include, url
from mainproject import views

urlpatterns = patterns('',
                       url(r'^$', views.mainpage, name='mainpage'),
                       )
