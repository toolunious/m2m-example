# Generated by Django 2.0 on 2019-08-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2m', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='characteristics',
        ),
        migrations.AddField(
            model_name='plant',
            name='province',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'province'}, to='m2m.Characteristic'),
        ),
    ]
