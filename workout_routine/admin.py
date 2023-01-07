from django.contrib import admin
from workout_routine.models import Exercise, Workout, WorkoutSet

class WorkoutSetInline(admin.TabularInline):
    model = WorkoutSet

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [
        WorkoutSetInline,
    ]

admin.site.register(Exercise)
admin.site.register(Workout, WorkoutAdmin)
