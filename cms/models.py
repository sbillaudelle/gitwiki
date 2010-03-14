from django.db import models

class PageType(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    markup = models.CharField(max_length=100, choices=(
                                ('restructuredtext', 'reStructuredText'),
                                ('html', 'HTML'),
                                ('template', 'Django Template')
                                ))
    layout = models.TextField()


    def __unicode__(self):
        return "PageType '{0}' (uses '{1}' markup)".format(self.id, self.markup)


class Page(models.Model):

    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    visible = models.BooleanField()
    position = models.IntegerField()


    def __unicode__(self):
        return "Page '{0}'".format(self.title)


class Redirection(models.Model):

    url = models.CharField(max_length=200, primary_key=True)
    destination = models.CharField(max_length=200)


    def __unicode__(self):
        return "Redirection from '{0}' to '{1}'".format(self.url, self.destination)
