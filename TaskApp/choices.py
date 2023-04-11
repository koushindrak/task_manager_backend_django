from django.db import models

class TaskPriority(models.TextChoices):
    HIGH = 'HIGH'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'

class TaskStatus(models.TextChoices):
    TO_DO = 'TODO'
    IN_PROGRESS = 'INPROGRESS'
    DONE = 'DONE'