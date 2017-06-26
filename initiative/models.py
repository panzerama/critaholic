from django.db import models
from django.core.urlresolvers import reverse


class Encounter(models.Model):

    def get_absolute_url(self):
        return reverse('init view', args=[self.id])


class Initiative(models.Model):
    creature_name = models.TextField(blank=False)
    initiative_value = models.IntegerField(default=0)
    hit_points = models.IntegerField(default=1)
    encounter = models.ForeignKey(Encounter, default=None)
    turn_order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.turn_order == 0:
            self.turn_order = Initiative.objects.filter(encounter=self.encounter).count() + 1
        super(Initiative, self).save(*args, **kwargs)


    class Meta:
        ordering = ['turn_order']
