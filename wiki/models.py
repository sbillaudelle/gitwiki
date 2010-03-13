from django.db import models

class Page(models.Model):

    path = models.CharField(max_length=500, primary_key=True)
    hash = models.CharField(max_length=64)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()


class PageType(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    markup = models.CharField(max_length=100, choices=(
                                ('restructuredtext', 'reStructuredText'),
                                ('html', 'HTML')
                                ))
    layout = models.TextField()
