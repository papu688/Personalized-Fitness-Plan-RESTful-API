from rest_framework import generics, permissions
from .models import Workout, WorkoutPlan, NutritionPlan, WorkoutProgress
from .serializers import WorkoutSerializer, WorkoutPlanSerializer, NutritionPlanSerializer, WorkoutProgressSerializer


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
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer): #Beim Erstellen wird das Feld user automatisch mit dem aktuell angemeldeten Benutzer (self.request.user) verknüpft.
        serializer.save(user=self.request.user)

    def get_queryset(self): #nur die Workout-Pläne des aktuellen Benutzers zurückgeben
        return WorkoutPlan.objects.filter(user=self.request.user)

class WorkoutPlanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)
    
class NutritionPlanListCreateAPIView(generics.ListCreateAPIView):
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return NutritionPlan.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NutritionPlanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)
