# Generated by Django 2.1.3 on 2018-11-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0002_journey_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='timestamp',
            field=models.DateField(help_text='journey date'),
        ),
    ]
