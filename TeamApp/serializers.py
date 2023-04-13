from rest_framework import serializers

from .models import Teams


class TeamSerializer(serializers.ModelSerializer):
    # users = UserResponseSerializer(many=True)

    class Meta:
        model = Teams
        # fields = '__all__'
        exclude = ('users',)
