from django.test import TestCase
from django.urls import reverse

from .models import CustomUser
# Create your tests here.


class UserRegistrationsTest(TestCase):
    def test_create_user(self):
        self.client(
            reverse('users:regis'),
            data = {
                'username':'OYBEK2004',
                'first_name':'OYBEK',
                'last_name':'ISROILOV',
                'email':'oisroilov173@gmail.com',
                'password':'2004'
            }
        )
        user = CustomUser.objects.get_user(self.client)
        self.assertEqual(user.username, 'OYBEK2004'),
        self.assertEqual(user.last_name, 'OYBEK'),
        self.assertEqual(user.first_name, 'ISROILOV'),
        self.assertEqual(user.email, 'oisroilov173@gmail.com')

    def test_required_fields(self):
        self.client.post(
            reverse('users:regis'),
            data={
                'first_name': 'OYBEK',
                'last_name': 'ISROILOV',

            }
        )
        user_cnt = CustomUser.objects.count()
        self.assertEqual(user_cnt, 0)

    def test_email_regis(self):
        self.client.post(
            reverse('users:regis'),
            data={
                'username':'OYBEK2004',
                'first_name':'OYBEK',
                'last_name':'ISROILOV',
                'email':'oisroilov173@gmail.com',
                'password':'2004'
            }
        )
        user_cnt = CustomUser.objects.count()
        self.assertEqual(user_cnt, 0)
        self.assertTrue(res, 'Enter a valid email adress.')


class LoginTest(TestCase):
    def test_login(self):
        self.client(
            reverse('users:regis'),
            data = {
                'username':'OYBEK2004',

                'password':'2004'
            }
        )
        user_is = get_user(self.client)
        self.assertFalse(user.username, 'OYBEK2004'),

