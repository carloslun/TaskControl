from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
#from .models import Login
#from .serializers import LoginSerializer

# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pass