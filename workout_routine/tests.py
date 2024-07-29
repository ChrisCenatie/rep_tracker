from django.test import TestCase
from workout_routine.models import Exercise, Workout, WorkoutSet

class WorkoutTestCase(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(name="Bench Press", description="Add weight to barbell and push")
        self.workout = Workout.objects.create(exercise=self.exercise)

    def test_workout_str_representation_is_exercise_name(self):
        self.assertEqual(str(self.workout), self.exercise.name)

class WorkoutSetTestCase(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(name="Bench Press", description="Add weight to barbell and push")
        self.workout = Workout.objects.create(exercise=self.exercise)
        self.workout_set = WorkoutSet.objects.create(workout=self.workout,reps=8)

    def test_workout_set_str_representation_displays_workout_and_number_of_reps(self):
        self.assertEqual(str(self.workout_set), f'{self.exercise.name}: {self.workout_set.reps} reps')
