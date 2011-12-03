from time import mktime
from django.db import models


class Minimizer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.timestamp)

    @property
    def timestamp(self):
        return int(mktime(self.created_at.timetuple()))

    class Meta:
        ordering = ('-created_at',)
        get_latest_by = ('created_at',)
