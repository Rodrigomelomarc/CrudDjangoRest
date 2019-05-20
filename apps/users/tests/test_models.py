from django.test import TestCase
from model_mommy import mommy
from apps.users.models import User


class TestUser(TestCase):

    def setUp(self):
        self.user = mommy.make(
            User,
            id=123,
            name='Rodrigo de Melo',
            email='rodrigomelomarcolino@gmail.com',
            password='123456'
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
