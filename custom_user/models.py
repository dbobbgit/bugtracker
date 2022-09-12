from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    # email = models.EmailField(max_length=50)
    # password = models.CharField(max_length=25)

    def __str__(self):
        return self.username
