from time import mktime
from django.db import models


class Minimizer(models.Model):
    script_name = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.script_name

    def save(self, *args, **kwargs):
        if not self.script_name:
            timestamp = mktime(self.created_at.timetuple())
            self.script_name = 'min.%s.js' % timestamp
        return super(Minimizer, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
        get_latest_by = ('created_at',)
