from django.db import models

class Page(models.Model):

    path = models.CharField(max_length=500, primary_key=True)
    hash = models.CharField(max_length=64)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()
