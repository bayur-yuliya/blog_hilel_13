from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    updated_at = models.DateTimeField(blank=True, auto_now=True)
