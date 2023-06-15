from django.urls import include, path
from rest_framework import routers

from .views import GroupViewSet, StudentViewSet, MarkCreateView, FeedbackViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'feedbacks', FeedbackViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('mark-create/', MarkCreateView.as_view(), name='mark_create'),
]

urlpatterns += router.urls
