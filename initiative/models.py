from django.db import models

class Initiative(models.Model):
	creature_name = models.TextField
	initiative_order = models.IntegerField
