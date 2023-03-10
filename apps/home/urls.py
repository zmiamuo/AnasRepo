# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home import views 


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('home/notifications.html', views.notifwebsites,name="notifwebsites"),
    path('home/user.html', views.updateuser, name='updateuser'),
    path('/getLogs', views.getLogs,name="getLogs"),
    path('/getLogs_json', views.getLogs_json,name="getLogs_json"),
    path('/*', views.ip_request,name="ip_request"),

    
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
