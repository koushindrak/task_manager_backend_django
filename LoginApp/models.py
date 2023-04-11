from django.db import models

import AppUsers.models
from LoginApp.TokenType import TokenType
from task_manager3.models import BaseModel


class LoginDetails(BaseModel):
    is_expired = models.BooleanField(null=True)
    logged_in_time = models.DateTimeField()
    logged_out_time = models.DateTimeField(null=True)
    is_revoked = models.BooleanField(null=True)
    token = models.CharField(max_length=255, unique=True)
    token_type = models.CharField(max_length=6, choices=TokenType.choices, default=TokenType.BEARER)  # BEARER

    # Relationships
    user = models.ForeignKey(AppUsers.models.AppUsers, on_delete=models.CASCADE,
                             related_name='_login_details')  # Many-to-One with User

    class Meta:
        db_table = 'login_details'

    def __str__(self):
        return f"{self.user} - {self.token}"

