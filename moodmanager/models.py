from django.db import models
from accounts.models import UserProfile
from .managers import MoodLogManager
from .constants import MOOD_CHOICES

# Create your models here.

class MoodLog(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='mood_logs'
    )

    mood = models.CharField(
        max_length=10,
        choices=MOOD_CHOICES
    )

    energy = models.PositiveSmallIntegerField()

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    objects = MoodLogManager()

    def __str__(self):
        return f"{self.user.user_name} - {self.mood} ({self.energy})"
