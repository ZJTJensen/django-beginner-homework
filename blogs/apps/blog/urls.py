from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^create$', views.create),     # This line has changed!
    url(r'^$', views.create),
    url(r'^blogs', views.index),
    url(r'^blogs/new', views.new),
    url(r'^blogs/newcreate', views.newcreate),
    url(r'^blogs/show', views.show),
    url(r'^blogs/edit', views.edit),
    url(r'^blogs/destroy', views.destroy)
  ]


