from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chat import views

router = DefaultRouter()
router.register('room', views.ChatRoomViewSet)
router.register('messages', views.MessageViewSet, basename='Message')

app_name = 'chat'

urlpatterns = [
    path('', include(router.urls)),
]
