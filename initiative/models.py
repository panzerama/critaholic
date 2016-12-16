from django.db import models


class Initiative(models.Model):
    creature_name = models.TextField(default='')
    initiative_value = models.IntegerField(default=0)

    class Meta:
        ordering = ['-initiative_value']
