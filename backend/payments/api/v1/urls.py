from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register('payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('add-payment-method/', AddPaymentMethodView.as_view()),
    path('checkout/', CheckoutView.as_view()),
    path('', include(router.urls)),
]
