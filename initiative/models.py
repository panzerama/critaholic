from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist


class Encounter(models.Model):

    def get_absolute_url(self):
        return reverse('view', args=[self.id])


class Initiative(models.Model):
    creature_name = models.TextField(blank=False)
    initiative_value = models.IntegerField(default=0)
    hit_points = models.IntegerField(default=1)
    encounter = models.ForeignKey(Encounter, default=None)
    turn_order = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if self.turn_order is None:
            try:
                self.turn_order = Initiative.objects.filter(encounter=self.encounter).count()+1
            except ObjectDoesNotExist:
                self.turn_order = 1
        super(Initiative, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-initiative_value']
