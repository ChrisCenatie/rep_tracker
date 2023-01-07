from django.test import TestCase
from workout_routine.models import Exercise, Workout

class WorkoutTestCase(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(name="Bench Press", description="Add weight to barbell and push")
        self.workout = Workout.objects.create(exercise=self.exercise)

    def test_workout_str_representation_is_exercise_name(self):
        self.assertEqual(str(self.workout), self.exercise.name)
