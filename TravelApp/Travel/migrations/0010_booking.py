# Generated by Django 5.0.2 on 2024-02-28 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0009_rename_user_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_people', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travel.tour')),
            ],
        ),
    ]
