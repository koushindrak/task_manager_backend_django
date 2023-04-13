from rest_framework import serializers, viewsets

from LabelApp.models import Labels
from LabelApp.serializer import LabelSerializer
from ProjectApp.models import Projects
from ProjectApp.serializers import ProjectSerializer
from TeamApp.models import Teams
from TeamApp.serializers import TeamSerializer
from .models import Tasks
from rest_framework import serializers
from datetime import datetime


class UnixTimestampField(serializers.Field):
    def to_representation(self, value):
        return int(value.timestamp() * 1000)

    def to_internal_value(self, data):
        return datetime.fromtimestamp(int(data) / 1000)


from rest_framework import serializers
from datetime import timedelta
import time

class TaskRequestSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField(required=False)
    team = serializers.PrimaryKeyRelatedField(queryset=Teams.objects.all(), required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), required=False)
    labels = serializers.PrimaryKeyRelatedField(queryset=Labels.objects.all(), many=True, required=False)

    class Meta:
        model = Tasks
        exclude = ('user',)

    def validate(self, attrs):
        attrs['name'] = attrs.get('name', None)
        if not attrs['name']:
            raise serializers.ValidationError("The 'name' field is mandatory.")

        attrs['description'] = attrs.get('description', None)
        attrs['due_date'] = attrs.get('due_date', None) or time.time() + 24*60*60*1000
        attrs['status'] = attrs.get('status', None) or 'TODO'
        attrs['priority'] = attrs.get('priority', None) or 'MEDIUM'
        return attrs


class TaskSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Teams.objects.all(), required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), required=False)
    labels = serializers.PrimaryKeyRelatedField(queryset=Labels.objects.all(), many=True, required=False)

    class Meta:
        model = Tasks
        exclude = ('user',)


class TaskResponseSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Tasks
        exclude = ('user',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['teamId'] = data['team']['id'] if data['team'] else None
        data['teamName'] = data['team']['name'] if data['team'] else None
        data['projectId'] = data['project']['id'] if data['project'] else None
        data['projectName'] = data['project']['name'] if data['project'] else None
        data['labels'] = [{"id": label['id'], "name": label['name']} for label in data['labels']]

        data.pop('team')
        data.pop('project')

        return data
