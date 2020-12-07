from rest_framework import generics
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
import requests
import json

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


def login(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/room/default')

    return render(request, "login.html", {'login_form': form})


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('/login')

    return render(request, "signup.html", {'signup_form': form})


def chatroom_messages(request):
    url = "http://localhost:8000/api/chat/messages/"

    querystring = {"chat_room": "default"}

    payload = ""
    headers = {'Authorization': 'Token b3f8b1d563cd546ab3025f3cf449e1495676b486'}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return render(request, "chatroom.html", {'chat_messages': json.loads(response.text), 'room_name': 'default'})
