from django.shortcuts import render
from rest_framework import generics
from .models import Login
from .serializers import LoginSerializer

# Create your views here.
class LoginView(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    pass
