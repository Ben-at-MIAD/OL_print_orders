from django.conf.urls import url
#from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploads/form/$', views.submit_stl, name='submit_stl'),
]
