from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.ListBookView.as_view()),
    path('create', csrf_exempt(views.CreateBookView.as_view())),
    path('retrieve/<int:pk>', csrf_exempt(views.RetrieveBookView.as_view())),
    path('update/<int:pk>', csrf_exempt(views.UpdateBookView.as_view())),
    path('delete/<int:pk>', csrf_exempt(views.DeleteBookView.as_view()))
]