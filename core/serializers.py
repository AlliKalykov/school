from .models import Group, Student, Mark, Feedback
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'telegram_id', 'text', 'first_name', 'last_name', 'date', 'rate')
        read_only_fields = ('id', 'date')
        

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
    

class MailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    from_email = serializers.EmailField()
    recipient_list = serializers.ListField(child=serializers.EmailField())


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()
