from rest_framework import serializers

from core.models import ChatRoom, Message


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id', 'name')
        read_only_fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'room', 'content', 'created_on')
        read_only_fields = ('id',)
