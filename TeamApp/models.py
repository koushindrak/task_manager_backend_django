from django.db import models

from AppUsers.models import AppUsers
from ProjectApp.ProjectStatus import EntityStatus
from task_manager3.models import BaseModel


class Teams(BaseModel):
    description = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=8, choices=EntityStatus.choices,
                              default=EntityStatus.ACTIVE)  # ACTIVE or INACTIVE
    users = models.ManyToManyField(AppUsers, related_name="_teams")

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name