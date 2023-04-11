from django.db import models

from AppUsers.models import AppUsers
from task_manager3.models import BaseModel


class Labels(BaseModel):
    description = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=20)
    # Relationships
    user = models.ForeignKey(AppUsers, on_delete=models.CASCADE, related_name='_labels')  # Many-to-One with User

    class Meta:
        db_table = 'labels'

    def __str__(self):
        return self.name