from rest_framework import serializers
from ProjectApp.models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ('user',)
        # fields = '__all__'
