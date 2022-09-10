from dataclasses import fields
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer): #Nombre  => Nombre del modelo+serializer 
    class Meta:
        model = User
        fields = ('password',
        'username',
        'is_usermain',
        'is_disenadorprocesos',
        'is_funcionario',
        'email',
        'first_name',
        'last_name')

# Continue Crete serializer here
