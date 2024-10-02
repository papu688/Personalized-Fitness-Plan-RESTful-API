from django.contrib import admin
from .models import User, Workout, NutritionPlan, WorkoutPlan, WorkoutProgress

admin.site.register(User)
admin.site.register(Workout)
admin.site.register(NutritionPlan)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutProgress)
