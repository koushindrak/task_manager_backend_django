from django.db import models

from TaskApp.models import Tasks
from task_manager3.models import BaseModel


class Comments(BaseModel):
    content = models.CharField(max_length=500)
    # Relationships
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='comments')  # Many-to-One with Task

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f"{self.task} - {self.content}"
