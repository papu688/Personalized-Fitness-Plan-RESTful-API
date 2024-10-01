from rest_framework import serializers
from .models import User

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'is_admin', 'created_at', 'updated_at']
        read_only_fields = ['is_admin', 'created_at', 'updated_at']