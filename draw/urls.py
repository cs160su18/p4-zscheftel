# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url('ingredientSelect', views.ingredientSelect, name='ingredientSelect'),
    url(r'custom', views.custom, name='custom'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

