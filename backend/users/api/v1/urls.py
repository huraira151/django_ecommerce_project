from django.urls import path, include
from .viewsets import SignUpViewSet, LoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('signup', SignUpViewSet, basename='signup')
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls))
]
