from rest_framework.generics import RetrieveAPIView, CreateAPIView,\
    ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoObjectPermissions

from .models import Book
from .serializers import BookSerializer


class CreateBookView(CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated


class RetrieveBookView(RetrieveAPIView):
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated


class ListBookView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()


class UpdateBookView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = DjangoObjectPermissions


class DeleteBookView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = DjangoObjectPermissions