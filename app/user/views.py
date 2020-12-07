from rest_framework import generics
from django.shortcuts import render

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")
