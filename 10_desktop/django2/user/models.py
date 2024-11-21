from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    has_cat = models.BooleanField(default=False)    # django가 초기 세팅할때 세팅잡기 어렵기때문에 가장 처음에 작성
