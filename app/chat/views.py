from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import ChatRoom, Message
from chat.serializers import ChatRoomSerializer, MessageSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ChatRoomViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = response.data
        return Response({'status': 'success', 'instance': instance})


class MessageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_name = self.request.query_params.get('chat_room')
        filter_room = ChatRoom.objects.filter(name=room_name)
        queryset = []
        if room_name is not None and filter_room.exists():
            queryset = Message.objects.filter(room=filter_room[0])

        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user
        room = ChatRoom.objects.get(name=request.data['room'])
        content = request.data['content']
        Message.objects.create(user=user, room=room, content=content)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
