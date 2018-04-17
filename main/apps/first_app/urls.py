from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.init), #any route that comes in goes to method init
    url(r'^random_word', views.index),
]  