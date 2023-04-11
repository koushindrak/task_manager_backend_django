from rest_framework import serializers

from LabelApp.models import Labels
from ProjectApp.models import Projects
from TeamApp.models import Teams
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Teams.objects.all(), required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), required=False)
    labels = serializers.PrimaryKeyRelatedField(queryset=Labels.objects.all(), many=True, required=False)

    class Meta:
        model = Tasks
        exclude = ('user', )
