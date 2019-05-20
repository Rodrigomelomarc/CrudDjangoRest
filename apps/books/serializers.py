from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        book.save()
        return book

    class Meta:
        model = Book
        fields = '__all__'
