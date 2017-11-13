from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'$', views.index)
]
urlpatterns = [
    url(r'$', views.new)
]
urlpatterns = [
    url(r'$', views.create)
]
urlpatterns = [
    url(r'$', views.show)
]
urlpatterns = [
    url(r'$', views.edit)
]
urlpatterns = [
    url(r'$', views.destroy)
]