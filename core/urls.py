from django.urls import include, path
from rest_framework import routers

from .views import GroupViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
