from django.db import models
from django.shortcuts import reverse


class Character(models.Model):
    character_name = models.TextField(blank=False, default='NPC')
    summary = models.TextField(default=' ')

    def get_absolute_url(self):
        return reverse('character view', args=[self.id])

# TODO better default values for character_name