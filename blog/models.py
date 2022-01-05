from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    categery = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    # slug = ... #TODO
    # is_published = models.BooleanField() #TODO
