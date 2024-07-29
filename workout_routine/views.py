from django.http import JsonResponse
from workout_routine.models import Exercise

# Create your views here.
def exercise_list(request):
    return JsonResponse(Exercise.json_list())
