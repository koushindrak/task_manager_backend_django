from rest_framework import serializers
from .models import AppUsers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = AppUsers.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = AppUsers
        fields = ('id', 'email', 'username', 'password')
