from django.urls import path
from .views import index, search_name, notify

urlpatterns = [
    path('', index),
    path('notify/', notify, name = 'notify'),
    path('search_name/', search_name, name = 'search_name'),
]