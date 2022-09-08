from tkinter import N
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# Create your models here.
class User(AbstractUser):
    is_administrador=models.BooleanField(default=False)
    is_disenadorprocesos=models.BooleanField(default=False)
    is_funcionario=models.BooleanField(default=False)

    def get_administrador_rol(self):
        admin_rol = None
        if hasattr(self,"administrador"):
            admin_rol = self.administrador
        return admin_rol







    class Meta:
        db_table = 'auth_user'

    objects = UserManager()

    def __str__(self):
        return self.username

# ROLES
class Administrador(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    objects = models.Manager()

class DiseñadorProcesos(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    objects = models.Manager()

class Funcionario(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    objects = models.Manager()