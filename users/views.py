from os import stat
from pyexpat import model
from django.http import HttpResponseRedirect, response
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .serializers import UserSerializer
from .models import User
from users import serializers
from django.contrib.auth.hashers import make_password

class main(APIView):
    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(request.data, status=status.HTTP_200_OK)

        else:
            return Response(request.data, status=status.HTTP_403_FORBIDDEN)


class signup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            name = serializer.data['name']
            username = serializer.data['username']
            password = make_password(serializer.data['password'])
            new_user = User(email=email, name=name, username=username, password=password)
            new_user.save()
            return Response(request.data, status=status.HTTP_201_CREATED)

        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)