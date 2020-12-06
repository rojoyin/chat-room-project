from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


user_payload = {'username': 'test', 'password': 'test123'}
chat_room_payload = {'name': 'testing'}


def create_user():
    return get_user_model().objects.create_user(**user_payload)


def create_chat_room():
    return models.ChatRoom.objects.create(**chat_room_payload)


class ModelTests(TestCase):
    def test_create_chat_room_ok(self):
        room = models.ChatRoom.objects.create(
            name='default'
        )
        self.assertEqual(str(room), room.name)

    def test_create_message_ok(self):
        user = create_user()
        room = create_chat_room()
        sample_content = 'hello'
        message = models.Message.objects.create(
            user=user, room=room, content=sample_content
        )
        self.assertEqual(message.user.username, user_payload['username'])
        self.assertEqual(message.room.name, chat_room_payload['name'])
        self.assertEqual(message.content, sample_content)
