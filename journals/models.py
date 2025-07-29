from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    """Model a task."""
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, editable=False
        )
    daily_prompt = models.CharField()
    gratitude_section = models.TextField()
    goals = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField()

    def __str__(self):
        """Return a string representation of the model."""
        return f'{self.title.lower()}'
