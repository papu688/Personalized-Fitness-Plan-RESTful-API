import django_filters
from .models import Workout

class WorkoutFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    target_muscles = django_filters.CharFilter(field_name='target_muscles', lookup_expr='icontains')
    
    class Meta:
        model = Workout
        fields = ['name', 'target_muscles']