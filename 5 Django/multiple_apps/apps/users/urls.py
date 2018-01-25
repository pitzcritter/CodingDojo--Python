from django.conf.urls import url
from . import views

urlpatterns = [

    # /users 
    url(r'^$', views.index),
    # /users/new
    url(r'^new$', views.register),
    # /register
    url(r'^register$', views.register),
    # /login 
    url(r'^login$', views.login),

]