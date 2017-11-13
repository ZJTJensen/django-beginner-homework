from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
         # This line has changed!
    url(r'^$', views.index),
    url(r'^generate$', views.generate),
    url(r'^reset$', views.reset)
  ]