from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated, IsAdminUser, DjangoModelPermissions

from .models import Group, Student, Mark
from .serializers import GroupSerializer, StudentSerializer, MarkCreateSerializer
from .permissions import IsTeacher, IsStudent

class GroupViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsTeacher]

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['group']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name', 'group']

    permission_classes = [IsStudent | IsTeacher]


class MarkCreateView(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkCreateSerializer