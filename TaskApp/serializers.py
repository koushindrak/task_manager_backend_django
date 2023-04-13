from rest_framework import serializers, viewsets

from LabelApp.models import Labels
from ProjectApp.models import Projects
from TeamApp.models import Teams
from TeamApp.serializers import TeamSerializer
from .models import Tasks
from datetime import datetime
from rest_framework import serializers
from datetime import timedelta
import time


class UnixTimestampField(serializers.Field):
    def to_representation(self, value):
        return int(value.timestamp() * 1000)

    def to_internal_value(self, data):
        return datetime.fromtimestamp(int(data) / 1000)


class TaskRequestSerializer(serializers.ModelSerializer):
    due_date = UnixTimestampField(required=False)
    project_id = serializers.IntegerField(allow_null=True,required=False)
    label_id = serializers.IntegerField(allow_null=True,required=False)

    class Meta:
        model = Tasks
        fields = ['id', 'name', 'description', 'due_date', 'status', 'priority', 'project_id', 'label_id']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        label_id = validated_data.pop('label_id', None)
        task = super().create(validated_data)
        if label_id is not None:
            label = Labels.objects.get(pk=label_id)
            task.labels.add(label)
        return task


class TaskSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Teams.objects.all(), required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), required=False)
    labels = serializers.PrimaryKeyRelatedField(queryset=Labels.objects.all(), many=True, required=False)

    class Meta:
        model = Tasks
        exclude = ('user',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = ['id', 'name']


class TaskResponseSerializer2(serializers.ModelSerializer):
    # project = ProjectSerializer()
    project_id = serializers.IntegerField(source='project.id', allow_null=True)
    project_name = serializers.CharField(source='project.name', allow_null=True)
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'name', 'status', 'description', 'due_date', 'description', 'project_id', 'project_name',
                  'labels']


class TaskResponseSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Tasks
        exclude = ('user',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['team_id'] = data['team']['id'] if data['team'] else None
        # data['team_name'] = data['team']['name'] if data['team'] else None
        # data['project_id'] = data['project']['id'] if data['project'] else None
        # data['project_name'] = data['project']['name'] if data['project'] else None
        # data['labels'] = [{"id": label['id'], "name": label['name']} for label in data['labels']]
        #
        # data.pop('team')
        # data.pop('project')

        return data
