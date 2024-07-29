import datetime
from django.test import TestCase
from django.db.utils import IntegrityError
from workout_routine.models import Exercise, Workout, WorkoutSet

class ExerciseTetstCase(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(name="Bench Press", description="Add weight to barbell and push")

    def test_exercise_instances_must_have_a_unique_name(self):
        with self.assertRaises(IntegrityError) as e:
            Exercise.objects.create(name="Bench Press", description="Can't have same Name")

        exception = e.exception
        self.assertIsInstance(exception, IntegrityError)

class WorkoutTestCase(TestCase):
    def setUp(self):
        self.workout_datetime = datetime.datetime.now()
        self.exercise = Exercise.objects.create(name="Bench Press", description="Add weight to barbell and push")
        self.workout = Workout.objects.create(exercise=self.exercise, datetime=self.workout_datetime)

    def test_workout_str_representation_is_exercise_name(self):
        self.assertEqual(str(self.workout), self.exercise.name)

class WorkoutSetTestCase(TestCase):
    def setUp(self):
        self.workout_datetime = datetime.datetime.now()
        self.exercise = Exercise.objects.create(name="Bench Press", description="Add weight to barbell and push")
        self.workout = Workout.objects.create(exercise=self.exercise, datetime=self.workout_datetime)
        self.workout_set = WorkoutSet.objects.create(workout=self.workout,reps=8)

    def test_workout_set_str_representation_displays_workout_and_number_of_reps(self):
        self.assertEqual(str(self.workout_set), f'{self.exercise.name}: {self.workout_set.reps} reps')
