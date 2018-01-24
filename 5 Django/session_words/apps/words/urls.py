from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    #url(r'^$', views.words),     # This line has changed!
    url(r'^$', views.index),     # This line has changed!
    url(r'^words$', views.words),     # This line has changed!
    url(r'^words/add$', views.add_word),     # This line has changed!
    url(r'^words/clear$', views.clear)     # This line has changed!
]