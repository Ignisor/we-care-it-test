# Generated by Django 2.1.3 on 2018-11-15 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0003_auto_20181114_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journey',
            old_name='timestamp',
            new_name='date',
        ),
    ]
