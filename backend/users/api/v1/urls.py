from django.urls import path, include
from .viewsets import SignUpViewSet, LoginViewSet, ResetPasswordConfirmView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('signup', SignUpViewSet, basename='signup')
router.register('login', LoginViewSet, basename='login')
router.register('reset-password-confirm', ResetPasswordConfirmView, basename='reset-password-confirm')

urlpatterns = [
    path('', include(router.urls)),
    path('forgot-password/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]
