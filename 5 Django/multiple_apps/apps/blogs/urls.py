from django.conf.urls import url
from . import views 

urlpatterns = [
    #/blogs/
    url(r'^$', views.index),
    #/blogs/new/
    url(r'^new$', views.new),
    #/blogs/create/
    url(r'^create$', views.create),
    #/blogs/{{blog_id}}
    url(r'^(?P<blog_id>[0-9]+)$', views.show),
    #/blogs/{{number}}/edit
    url(r'^(?P<blog_id>[0-9]+)/edit$', views.edit),
    # /blogs/{{number}}/delete
    url(r'^(?P<blog_id>[0-9]+)/destroy$', views.destroy),

]
