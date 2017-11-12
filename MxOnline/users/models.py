from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=20,verbose_name='昵称')
    birthday=models.DateTimeField()
