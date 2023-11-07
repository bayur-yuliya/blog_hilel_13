from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
