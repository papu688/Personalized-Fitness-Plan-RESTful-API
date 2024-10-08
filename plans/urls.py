
from django.urls import path
from .views import (
    WorkoutListCreateAPIView,
    WorkoutDetailAPIView,
    WorkoutPlanListCreateAPIView,
    WorkoutPlanDetailAPIView,
    NutritionPlanListCreateAPIView,
    NutritionPlanDetailAPIView,
    WorkoutProgressListCreateAPIView,
    WorkoutProgressDetailAPIView,
    
)

urlpatterns = [
    path('workouts/', WorkoutListCreateAPIView.as_view(), name='workout-list-create'),
    path('workouts/<int:pk>/', WorkoutDetailAPIView.as_view(), name='workout-detail'),
    path('workouts/batch-delete/', WorkoutListCreateAPIView.as_view()),

    path('workout-plans/', WorkoutPlanListCreateAPIView.as_view(), name='workout-plan-list-create'),
    path('workout-plans/<int:pk>/', WorkoutPlanDetailAPIView.as_view(), name='workout-plan-detail'),
    path('workout-plans/batch-delete/', WorkoutPlanListCreateAPIView.as_view()),
    
    path('nutrition-plans/', NutritionPlanListCreateAPIView.as_view(), name='nutrition-plan-list-create'),
    path('nutrition-plans/<int:pk>/', NutritionPlanDetailAPIView.as_view(), name='nutrition-plan-detail'),
    path('nutrition-plans/batch-delete/', NutritionPlanListCreateAPIView.as_view()),

    path('workout-progress/', WorkoutProgressListCreateAPIView.as_view(), name='workout-progress-list-create'),
    path('workout-progress/<int:pk>/', WorkoutProgressDetailAPIView.as_view(), name='workout-progress-detail'),
    path('workout-progress/batch-delete/', WorkoutProgressListCreateAPIView.as_view()),

]


