from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Group, Student, Mark, Feedback
from .serializers import GroupSerializer, StudentSerializer, MarkCreateSerializer, FeedbackSerializer
from .permissions import IsTeacher, IsStudent
from .paginations import CustomPagination

class GroupViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsTeacher | IsAdminUser]

    pagination_class = CustomPagination

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['group']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name', 'group']

    permission_classes = [IsStudent | IsTeacher | IsAdminUser]


class MarkCreateView(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkCreateSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rate']
    search_fields = ['text', 'first_name', 'last_name']
    ordering_fields = ['date', 'rate', 'first_name', 'last_name']
