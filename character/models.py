from django.db import models


class Character(models.Model):
    character_name = models.TextField(blank=False, default='NPC')
    summary = models.TextField(default=' ')

# TODO better default values for character_name