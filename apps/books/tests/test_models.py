from django.test import TestCase
from model_mommy import mommy
from apps.books.models import Book


class TestBook(TestCase):

    def setUp(self):
        self.book = mommy.make(
            Book, id=1,
            title='O homem que calculava',
            author='Malba Tahan',
            genre='Romance'
        )

    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
