from .models import Group, Student, Mark
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=False)
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'group')


class MarkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('id', 'mark', 'student', 'subject', 'date')
        read_only_fields = ('id', 'date')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = StudentSerializer(instance.student).data
        # representation['subject'] = serializers.StringRelatedField().data
        return representation
