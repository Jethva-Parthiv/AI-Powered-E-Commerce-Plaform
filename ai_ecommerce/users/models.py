from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    preferences = models.JSONField(default=dict, blank=True)  # Optional: store user category preferences

    def __str__(self):
        return self.username
