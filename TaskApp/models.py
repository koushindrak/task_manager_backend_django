from django.db import models

import LabelApp.models
import ProjectApp.models
from AppUsers.models import AppUsers
from TaskApp.choices import TaskPriority, TaskStatus
from TeamApp.models import Teams
from task_manager3.models import BaseModel


class Tasks(BaseModel):
    description = models.CharField(max_length=255, null=True)
    due_date = models.DateTimeField(null=True)
    name = models.CharField(max_length=50)
    priority = models.CharField(max_length=6, choices=TaskPriority.choices,
                                default=TaskPriority.MEDIUM)  # HIGH, LOW, MEDIUM
    status = models.CharField(max_length=10, choices=TaskStatus.choices,
                              default=TaskStatus.TO_DO)  # TODO, INPROGRESS, DONE

    # Relationships
    user = models.ForeignKey(AppUsers, on_delete=models.CASCADE, related_name='_tasks', null=True,
                             blank=True)  # Many-to-One with User
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='_tasks', null=True,
                             blank=True)  # Many-to-One with Group
    project = models.ForeignKey(ProjectApp.models.Projects, on_delete=models.CASCADE, related_name='_tasks', null=True,
                                blank=True)  # Many-to-One with Project

    labels = models.ManyToManyField(LabelApp.models.Labels, related_name='_tasks',
                                    blank=True)  # Many-to-Many with Label

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return self.name



