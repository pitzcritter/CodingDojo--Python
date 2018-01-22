from django.conf.urls import url#, patterns
#from apps.date_time import views
from . import views
#urlpatterns = patterns('',
#    url(r'^$', views.index, name='index'),
#)
urlpatterns = [
    url(r'^$', views.index, name='index'),
]