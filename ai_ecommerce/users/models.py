from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    preferences = models.JSONField(default=dict, blank=True)  # e.g., {"categories": ["electronics","books"]}
