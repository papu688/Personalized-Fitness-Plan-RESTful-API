from rest_framework import serializers
from .models import User, Workout, WorkoutPlan, NutritionPlan, WorkoutProgress

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'is_admin', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                name=validated_data['name'],
                is_admin=validated_data.get('is_admin', False)
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        
        def update(self, instance, validated_data):
            instance.email = validated_data('email', instance.email)
            instance.name = validated_data.get('name', instance.name)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.is_admin = validated_data.get('is_admin', instance.is_admin)

            password = validated_data.get('password', None)
            if password:
                instance.set_password(password)

            instance.save()
            return instance

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

    def validate_name(self, value):
        if Workout.objects.filter(name=value).exists():
            raise serializers.ValidationError("A workout with this name already exists")
        return value
        
class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError("The start date cannot be later than the end date.")
        return attrs
        
class NutritionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionPlan
        fields = '__all__'

class WorkoutProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgress
        fields = '__all__'


