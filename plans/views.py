from rest_framework import generics, permissions
from .models import Workout, WorkoutPlan, NutritionPlan, WorkoutProgress
from .serializers import WorkoutSerializer, WorkoutPlanSerializer, NutritionPlanSerializer, WorkoutProgressSerializer
from .filters import WorkoutFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from django.core.cache import cache
from rest_framework.response import Response

class UserOwnedMixin:
    """Mixin to filter objects by the logged-in user."""
    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        else:
            return super().get_queryset().filter(user=self.request.user)
        
class BatchDeleteMixin:
    """Mixin to handle batch deletion of objects."""
    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])
        if not ids:
            return Response({"detail": "No IDs provided."}, status=status.HTTP_400_BAD_REQUEST)

        deleted, _ = self.get_queryset().filter(id__in=ids).delete()
        return Response({"detail": f"{deleted} items deleted."}, status=status.HTTP_204_NO_CONTENT)


class WorkoutListCreateAPIView(BatchDeleteMixin, generics.ListCreateAPIView):
    """View for listing and creating workouts."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkoutFilter
    
    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class WorkoutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting workouts."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkoutPlanListCreateAPIView(UserOwnedMixin, BatchDeleteMixin, generics.ListCreateAPIView):
    """View for listing and creating workout plans."""
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Saves the workout plan with the currently logged-in user."""
        print('incoming data:', self.request.data)
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        cache_key = "workout_plans_list"
        cache_time = 60 * 5
        data = cache.get(cache_key)
        if not data:
            workout_plans = self.get_queryset()
            data = self.serializer_class(workout_plans, many=True).data
            cache.set(cache_key, data, cache_time)

        return Response(data)
        


class WorkoutPlanDetailAPIView(UserOwnedMixin, generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting workout plans."""
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class NutritionPlanListCreateAPIView(UserOwnedMixin, BatchDeleteMixin, generics.ListCreateAPIView):
    """View for listing and creating nutrition plans."""
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Saves the nutrition plan with the currently logged-in user."""
        serializer.save(user=self.request.user)


class NutritionPlanDetailAPIView(UserOwnedMixin, generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting nutrition plans."""
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkoutProgressListCreateAPIView(UserOwnedMixin, BatchDeleteMixin, generics.ListCreateAPIView):
    """View for listing and creating workout progress."""
    queryset = WorkoutProgress.objects.all()
    serializer_class = WorkoutProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Saves the workout progress with the currently logged-in user."""
        serializer.save(user=self.request.user)


class WorkoutProgressDetailAPIView(UserOwnedMixin, generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting workout progress."""
    queryset = WorkoutProgress.objects.all()
    serializer_class = WorkoutProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)