from dataclasses import fields
from distutils.log import Log
from rest_framework import serializers
from .models import Login

class LoginSerializer(serializers.ModelSerializer): #Nombre  => Nombre del modelo+serializer 
    class Meta:
        model = Login
        fields = ('title',
        'errorMessage',
        'labelButton')

# Continue Crete serializer here
