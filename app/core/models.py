from django.db import models
from django.contrib.auth import get_user_model


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    processed_by_bot = models.BooleanField(default=False)
