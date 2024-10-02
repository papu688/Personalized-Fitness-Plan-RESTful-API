from rest_framework import generics, permissions
from .models import Workout, WorkoutPlan, NutritionPlan, WorkoutProgress
from .serializers import WorkoutSerializer, WorkoutPlanSerializer, NutritionPlanSerializer, WorkoutProgressSerializer


class UserOwnedMixin:
    """Mixin zur Filterung von Objekten nach dem angemeldeten Benutzer."""
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class WorkoutListCreateAPIView(generics.ListCreateAPIView):
    """View zum Auflisten und Erstellen von Workouts."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkoutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View zum Abrufen, Aktualisieren und Löschen von Workouts."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkoutPlanListCreateAPIView(UserOwnedMixin, generics.ListCreateAPIView):
    """View zum Auflisten und Erstellen von Workout-Plänen."""
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Speichert den Workout-Plan mit dem aktuell angemeldeten Benutzer."""
        serializer.save(user=self.request.user)


class WorkoutPlanDetailAPIView(UserOwnedMixin, generics.RetrieveUpdateDestroyAPIView):
    """View zum Abrufen, Aktualisieren und Löschen von Workout-Plänen."""
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class NutritionPlanListCreateAPIView(UserOwnedMixin, generics.ListCreateAPIView):
    """View zum Auflisten und Erstellen von Ernährungsplänen."""
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Speichert den Ernährungsplan mit dem aktuell angemeldeten Benutzer."""
        serializer.save(user=self.request.user)


class NutritionPlanDetailAPIView(UserOwnedMixin, generics.RetrieveUpdateDestroyAPIView):
    """View zum Abrufen, Aktualisieren und Löschen von Ernährungsplänen."""
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkoutProgressListCreateAPIView(UserOwnedMixin, generics.ListCreateAPIView):
    """View zum Auflisten und Erstellen von Workout-Fortschritten."""
    queryset = WorkoutProgress.objects.all()
    serializer_class = WorkoutProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Speichert den Workout-Fortschritt mit dem aktuell angemeldeten Benutzer."""
        serializer.save(user=self.request.user)


class WorkoutProgressDetailAPIView(UserOwnedMixin, generics.RetrieveUpdateDestroyAPIView):
    """View zum Abrufen, Aktualisieren und Löschen von Workout-Fortschritten."""
    queryset = WorkoutProgress.objects.all()
    serializer_class = WorkoutProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)