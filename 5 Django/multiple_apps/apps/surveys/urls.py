from django.conf.urls import url
from . import views 

urlpatterns = [

# /surveys 
    url(r'^$', views.index),
# /surveys/new
    url(r'^new$', views.new),
]