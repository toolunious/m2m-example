from django.db import models

class Characteristic(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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
