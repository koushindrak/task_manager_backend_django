from django.db import models

from AppUsers.models import AppUsers
from TaskApp.models import Tasks
from task_manager3.models import BaseModel


class Notifications(BaseModel):
    description = models.CharField(max_length=255)
    message = models.TextField()

    # Relationships
    user = models.ForeignKey(AppUsers, on_delete=models.CASCADE, related_name="_notifications")
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='_notifications')  # Many-to-One with Task

    class Meta:
        db_table = 'notifications'

    def __str__(self):
        return f"{self.user} - {self.message}"