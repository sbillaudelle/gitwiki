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
        return "PageType '%s' (uses '%s' markup)" % (self.id, self.markup)
