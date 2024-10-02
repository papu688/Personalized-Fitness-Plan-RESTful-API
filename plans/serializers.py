from rest_framework import serializers
from .models import User

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