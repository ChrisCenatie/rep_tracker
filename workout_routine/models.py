from django.db import models
from django.core.validators import MinValueValidator

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Workout(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField(blank=True,validators=[MinValueValidator(0)])
