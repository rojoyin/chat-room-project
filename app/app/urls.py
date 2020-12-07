from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from user.views import login, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/chat/', include('chat.urls')),
    path('auth/', obtain_auth_token),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('room/default', signup, name='chatroom'),
]
