from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GenericWebpageView.as_view(), name="start"),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^(?P<template>[\w-]+)/$', views.GenericWebpageView.as_view(), name='staticpage'),
]
