from rest_framework import serializers

from core.models import ChatRoom, Message
from user.serializers import UserSerializer


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id', 'name')
        read_only_fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Message
        fields = ('id', 'user', 'content', 'created_on')
        read_only_fields = ('id',)
