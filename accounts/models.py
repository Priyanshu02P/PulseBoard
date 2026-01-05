from django.db import models
from django.contrib.auth.models import User
from .constants import ROLE_CHOICES

# Create your models here.

#User auth model
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username}:{self.user.first_name} - {self.role}"
    
