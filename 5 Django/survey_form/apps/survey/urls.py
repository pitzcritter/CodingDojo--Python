from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    #url(r'^$', views.index),     # This line has changed!
    #url(r'^process$', views.process),
    #url(r'^result$', views.result),
    url(r'^go_back$', views.go_back),
    url(r'^$', views.index, name='index'),
    url(r'^process_input$', views.process_input, name='process_input'),
    url(r'^results$', views.view_results),#, name='view_results'),
#    url(r'^admin/', include(admin.site.urls)),
]
