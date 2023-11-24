from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta

def generate_token():
    return uuid.uuid4().hex[:16]

# Create your models here.
class Task(models.Model):
    is_public = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Task {self.id} - {'Public' if self.is_public else 'Private'} - {self.description}"
    
class Token(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=16, default=generate_token, unique=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=1)
        super(Token, self).save(*args, **kwargs)