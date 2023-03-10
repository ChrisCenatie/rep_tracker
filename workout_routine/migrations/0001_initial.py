# Generated by Django 4.1.4 on 2022-12-30 21:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout_routine.exercise')),
            ],
        ),
    ]
