from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

from task_manager3.models import BaseModel


class AppUsers(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    enabled = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    verification_code = models.CharField(max_length=64, null=True, blank=True)
    code_expired = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

    @classmethod
    def create_user(cls, email, username, password):
        user = cls.objects.create(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def __str__(self):
        return self.username
