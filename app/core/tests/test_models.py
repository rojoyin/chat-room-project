from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ModelTests(TestCase):
    def test_create_chat_room_ok(self):
        room = models.ChatRoom.objects.create(
            name='default'
        )
        self.assertEqual(str(room), room.name)
