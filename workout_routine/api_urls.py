from django.urls import path
from workout_routine import views

urlpatterns = [
    path('exercises/', views.exercise_list, name='exercise_list')
]
