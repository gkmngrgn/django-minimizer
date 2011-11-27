from datetime import datetime
from time import mktime
from django.db import models


class Minimizer(models.Model):
    script_name = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.script_name

    def save(self, *args, **kwargs):
        if not self.script_name:
            self.created_at = datetime.now()
            self.script_name = str(int(mktime(self.created_at.timetuple())))
        return super(Minimizer, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
        get_latest_by = ('created_at',)
