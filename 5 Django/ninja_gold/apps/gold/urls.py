from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^farm$', views.farm, name='goto_farm'),
    url(r'^cave$', views.cave, name='goto_cave'),
    url(r'^house$', views.house, name='goto_house'),
    url(r'^casino$', views.casino, name='goto_casino'),    
    url(r'^clear$', views.clear, name='clear'),    
]