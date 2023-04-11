from django.db import models


class BaseModel(models.Model):
    created_by = models.CharField(max_length=255, null=True, blank=True, default="system")
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
