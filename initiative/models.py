from django.db import models


class Encounter(models.Model):
    pass


class Initiative(models.Model):
    creature_name = models.TextField(default='')
    initiative_value = models.IntegerField(default=0)
    encounter = models.ForeignKey(Encounter, default=None)

    class Meta:
        ordering = ['-initiative_value']
