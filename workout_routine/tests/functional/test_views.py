from django.test import TestCase, Client
from workout_routine.models import Exercise

client = Client()

class ApiV1ExerciseListTestCase(TestCase):
    def setUp(self):
        self.bench = Exercise.objects.create(name="Bench Press", description="Add weight to barbell and push")
        self.curls = Exercise.objects.create(name="Bicep Curls", description="Use biceps to curl weight")

    def test_GET_request_returns_list_of_available_exercises(self):
        expected_content = {
            'exercises': [
                {'description': 'Add weight to barbell and push', 'exercise': 'Bench Press'},
                {'description': 'Use biceps to curl weight','exercise': 'Bicep Curls'}
            ]
        }
        resp = client.get('/api/v1/exercises/')

        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, expected_content)
