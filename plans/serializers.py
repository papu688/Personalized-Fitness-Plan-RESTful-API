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

    def validate_name(self, attrs):
        name = attrs.get('name')
        if Workout.objects.filter(name=name).exists():
            raise serializers.ValidationError("A workout with this name already exists")
        return attrs

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        # Überprüfe, ob beide Werte vorhanden sind
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("The start date cannot be later than the end date.")
        
        return attrs   #es sheamowme rato ar mushaobs

        
class NutritionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionPlan
        fields = '__all__'

class WorkoutProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgress
        fields = '__all__'


