# Generated by Django 5.0.2 on 2024-02-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0003_tour_description_tour_season_end_tour_season_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='mainstream',
            field=models.BooleanField(default=False),
        ),
    ]
