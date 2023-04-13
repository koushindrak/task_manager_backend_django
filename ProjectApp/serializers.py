from rest_framework import serializers
from ProjectApp.models import Projects
from rest_framework import serializers
from datetime import datetime


class UnixTimestampField(serializers.Field):
    def to_representation(self, value):
        return int(value.timestamp() * 1000)

    def to_internal_value(self, data):
        return datetime.fromtimestamp(int(data) / 1000)


class ProjectRequestSerializer(serializers.ModelSerializer):
    start_date = UnixTimestampField()
    end_date = UnixTimestampField()

    class Meta:
        model = Projects
        fields = ('name', 'description', 'status', 'start_date', 'end_date', 'status')
        # exclude = ('user',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ('user',)
        # fields = '__all__'
