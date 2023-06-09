from rest_framework import serializers

from TeamApp.models import Teams
from TeamApp.serializers import TeamSerializer
from .models import AppUsers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = AppUsers.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

    class Meta:
        model = AppUsers
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')


class TeamUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['id', 'name']


class UserResponseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    teams = TeamUserSerializer(many=True, read_only=True)

    def create(self, validated_data):
        user = AppUsers.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

    class Meta:
        model = AppUsers
        fields = (
        'id', 'email', 'username', 'password', 'first_name', 'last_name', 'is_superuser', 'last_login', 'date_joined',
        'teams')
