from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


class DraftPapersData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='draft-papers/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()