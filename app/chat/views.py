from django.shortcuts import render
from rest_framework import viewsets
from core.models import ChatRoom, Message
from chat.serializers import ChatRoomSerializer, MessageSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ChatRoomViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_query_set(self):
        room_name = self.request.query_params.get('chat_room')
        filter_room = ChatRoom.objects.create(
            name=room_name
        )
        return Message.objects.filter(room=filter_room)
