from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(models.Model):
    
    class Meta:
        db_table = 'auth_user'

    objects = models.Manager()

    def __str__(self):
        return "CustomUser"
