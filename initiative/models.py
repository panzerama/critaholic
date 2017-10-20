from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

class EncounterManager(models.Manager):
    def order_initiative_in_encounter(self):
        pass

class Encounter(models.Model):
    objects = EncounterManager()

    def get_absolute_url(self):
        return reverse('view', args=[self.id])


class Initiative(models.Model):
    creature_name = models.TextField(blank=False)
    initiative_value = models.IntegerField(default=0)
    hit_points = models.IntegerField(default=1)
    encounter = models.ForeignKey(Encounter, default=None)
    turn_order = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        try:
            set_turn_order = Initiative.objects.filter(encounter=self.encounter).count()+1
            self.turn_order = set_turn_order
        except ObjectDoesNotExist:
            self.turn_order = 1

        super(Initiative, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-initiative_value']
