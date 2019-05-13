from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.BookView.as_view({
        'get': 'list',
        'post': 'create'
    }))),
    path('<int:pk>', csrf_exempt(views.BookView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })))
]