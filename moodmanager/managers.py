from django.db import models

class MoodLogManager(models.Manager):
    def filter_logs(self, username=None, date=None, time=None):
        qs = self.get_queryset()

        if username:
            qs = qs.filter(user__user_name=username)

        if date:
            qs = qs.filter(date=date)

        if time:
            qs = qs.filter(time=time)

        return qs
