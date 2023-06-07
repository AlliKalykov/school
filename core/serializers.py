from .models import Group, Student
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

