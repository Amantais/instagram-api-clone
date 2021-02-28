from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterUserSerializer, UserInfoSerializer 


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user 
