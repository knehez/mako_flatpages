from django.conf.urls import url
from mako_flatpages import views

urlpatterns = [
    url(r'^(?P<url>.*)$', views.flatpage, name='mako_flatpages.views.flatpage'),
]
