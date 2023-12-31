from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class App_User(AbstractUser):
    email = models.EmailField(blank=False, null=False, unique=True, max_length=254)
    name = models.CharField(null = False, blank= False, max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name} | {self.email}"