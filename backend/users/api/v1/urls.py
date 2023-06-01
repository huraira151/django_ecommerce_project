from django.urls import path, include
from .viewsets import SignUpViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('signup', SignUpViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls))
]
