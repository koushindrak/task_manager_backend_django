from django.db import models

class TokenType(models.TextChoices):
    BEARER = 'BEARER'