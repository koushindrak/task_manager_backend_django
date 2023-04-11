from django.db import models

from AppUsers.models import AppUsers
from ProjectApp.ProjectStatus import ProjectStatus
from task_manager3.models import BaseModel


class Projects(BaseModel):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    status = models.CharField(max_length=8, choices=ProjectStatus.choices,
                              default=ProjectStatus.ACTIVE)  # ACTIVE or INACTIVE

    # Relationships
    user = models.ForeignKey(AppUsers, on_delete=models.CASCADE, related_name='_projects')  # Many-to-One with User

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.name