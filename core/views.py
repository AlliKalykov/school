from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters, status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Group, Student, Mark, Feedback
from .serializers import (
    GroupSerializer,
    StudentSerializer,
    MarkCreateSerializer,
    FeedbackSerializer,
    MailSerializer,
    EmailSerializer,
    ResetPasswordSerializer,
)
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
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["group"]
    search_fields = ["first_name", "last_name"]
    ordering_fields = ["first_name", "last_name", "group"]

    permission_classes = [IsStudent | IsTeacher | IsAdminUser]


class MarkCreateView(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkCreateSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["rate"]
    search_fields = ["text", "first_name", "last_name"]
    ordering_fields = ["date", "rate", "first_name", "last_name"]


from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response as DRFResponse


@api_view(["POST"])
def mailru_send_email(request):
    send_mail(
        subject="Тема почты",
        message="Основной текст",
        from_email="alli.kalykov@bk.ru",
        recipient_list=[
            "berikorynbasar522@mail.ru",
            "tonkih.ilya@mail.ru",
            "bekysmailov@mail.ru",
        ],
    )
    return DRFResponse({"message": "Письмо отправлено"})


from rest_framework.views import APIView


class MailSend(APIView):
    serializer_class = MailSerializer

    def post(self, request):
        serializer = MailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        send_mail(**serializer.validated_data)
        return DRFResponse({"message": "Письмо отправлено"})


from django.contrib.auth.models import User
from .models import ResetPassword

import random
import string


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(letters) for _ in range(length))
    return random_string


class ResetPasswordView(APIView):
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            token = generate_random_string(25)
            reset_url = f"http://127.0.0.1:8000/reset-password/?token={token}"
            ResetPassword.objects.create(email=email, token=token)
            # send_mail()
            return DRFResponse(
                status=status.HTTP_200_OK, data={"message": "Письмо отправлено"}
            )
        else:
            return DRFResponse(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "message": "Пользователь не найден! Проверьте правильность введенных данных"
                },
            )


class SetResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        pass
