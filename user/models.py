from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # phone_number = models.IntegerField(null=True, blank=True, help_text='optional')
    pass