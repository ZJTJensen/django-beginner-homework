from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^clocks/', views.index),     # This line has changed!
    url(r'^$', views.index)
  ]