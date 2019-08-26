from django.db import models

from m2m import constants

class Characteristic(models.Model):
    constants_id = models.IntegerField(null=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return dict(constants.DB_TYPES[self.type])[self.constants_id]


class Plant(models.Model):
    name = models.CharField(max_length=255)
    province = models.ManyToManyField(
        'Characteristic', blank=True,
        limit_choices_to={'type': 'province'}, related_name='province')
    
    color = models.ManyToManyField(
        'Characteristic', blank=True,
        limit_choices_to={'type': 'color'}, related_name='color')
    
    def __str__(self):
        return self.name
