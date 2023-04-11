from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

from task_manager3.models import BaseModel


# from common_app.Teams import Teams
# from common_app.BaseModel import BaseModel
# from common_app.AppRole import AppRoles
# from common_app.AppUsersRoles import AppUsersRoles
# from common_app.TeamsUsers import TeamsUsers


class AppUsers(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    enabled = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    verification_code = models.CharField(max_length=64, null=True, blank=True)
    code_expired = models.BooleanField(default=False)
    # Relationships
    # roles = models.ManyToManyField(AppRoles, through=AppUsersRoles, related_name='app_users')  # Many-to-Many with AppRoles
    # user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions")
    # teams = models.ManyToManyField(Teams, through=TeamsUsers)

    # user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set")
    class Meta:
        db_table = 'app_users'

    def __str__(self):
        return self.username
