from django.db import models
from django_markdown.models import MarkdownField


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    body = MarkdownField()

    def __unicode__(self):
      return self.title