from django.db import models
from django.core.urlresolvers import reverse


class Encounter(models.Model):

    def get_absolute_url(self):
        return reverse('view', args=[self.id])


class Initiative(models.Model):
    creature_name = models.TextField(blank=False)
    initiative_value = models.IntegerField(default=0)
    hit_points = models.IntegerField(default=1)
    encounter = models.ForeignKey(Encounter, default=None)
    turn_order = models.IntegerField(null=True)

    class Meta:
        ordering = ['-initiative_value']
