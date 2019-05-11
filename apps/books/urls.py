from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.BookView.as_view({'get': 'list'}))),
    path('store', csrf_exempt(views.BookView.as_view({'post': 'create'})))
]