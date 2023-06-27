from django.urls import include, path
from rest_framework import routers

from .views import GroupViewSet, StudentViewSet, MarkCreateView, FeedbackViewSet, mailru_send_email, MailSend, ResetPasswordView

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'feedbacks', FeedbackViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('mark-create/', MarkCreateView.as_view(), name='mark_create'),
    path('mailru_send_email/', mailru_send_email, name='mailru_send_email'),
    path('mail_send/', MailSend.as_view(), name='mail_send'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password')

]

urlpatterns += router.urls
