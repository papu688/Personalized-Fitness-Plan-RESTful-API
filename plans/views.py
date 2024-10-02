from rest_framework import generics, permissions
from .models import Workout, WorkoutPlan, NutritionPlan, WorkoutProgress
from .serializers import WorkoutSerializer, WorkoutPlanSerializer, NutritionPlan, WorkoutProgressSerializer


class WorkoutListCreateAPIView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WorkoutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class WorkoutPlanListCreateAPIView(generics.ListCreateAPIView):
