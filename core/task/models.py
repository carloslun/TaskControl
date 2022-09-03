from django.db import models

# Create your models here.
class Login(models.Model):
    title = models.CharField(max_length=50)
    errorMessage = models.CharField(max_length=100)
    labelButton = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.title
