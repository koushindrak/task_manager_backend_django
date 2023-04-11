from django.db import models


class ProjectStatus(models.TextChoices):
    ACTIVE = 'ACTIVE'
    IN_ACTIVE = 'INACTIVE'

class EntityStatus(models.TextChoices):
    ACTIVE = 'ACTIVE'
    IN_ACTIVE = 'INACTIVE'