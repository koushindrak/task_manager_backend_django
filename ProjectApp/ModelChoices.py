from django.db import models


class AppUserRoleTypes(models.TextChoices):
    ADMIN = 'ADMIN'
    USER = 'USER'


class TaskStatus(models.TextChoices):
    TO_DO = 'TODO'
    IN_PROGRESS = 'INPROGRESS'
    DONE = 'DONE'


class EntityStatus(models.TextChoices):
    ACTIVE = 'ACTIVE'
    IN_ACTIVE = 'INACTIVE'


class TaskPriority(models.TextChoices):
    HIGH = 'HIGH'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'


class TokenType(models.TextChoices):
    BEARER = 'BEARER'
