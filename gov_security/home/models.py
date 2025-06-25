from django.contrib.auth import get_user_model
from django.db import models

from departments.models import Department


class Message(models.Model):
    User = get_user_model()
    department = models.ForeignKey(
        Department, related_name="messages", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def str(self):
        return f"{self.author.username}: {self.message_text[:50]}"
