from django.db import models


class BaseModel(models.Model):
    created_by = models.CharField(max_length=255, null=True, blank=True, default="system")
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            # If the object is being created, set the created_by field
            user = getattr(self, 'user', None)
            if user is not None and user.is_authenticated:
                self.created_by = user.username
        else:
            # If the object is being updated, set the updated_by field
            user = getattr(self, 'user', None)
            if user is not None and user.is_authenticated:
                self.updated_by = user.username
        super().save(*args, **kwargs)
