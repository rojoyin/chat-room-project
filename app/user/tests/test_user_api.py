from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_ENDPOINT = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_ok(self):
        payload = {
            'username': 'rojoyin',
            'password': 'abc123',
        }
        res = self.client.post(CREATE_USER_ENDPOINT, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_already_exists(self):
        payload = {
            'username': 'rojoyin',
            'password': 'abc123',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_ENDPOINT, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_min_length(self):
        payload = {
            'username': 'rojoyin',
            'password': 'ab',
        }

        res = self.client.post(CREATE_USER_ENDPOINT, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user = get_user_model().objects.filter(
            username=payload['username']
        )
        self.assertFalse(user.exists())
