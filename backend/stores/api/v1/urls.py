from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('cart', CartViewSet, basename='cart')
router.register('add-to-cart', AddToCartViewSet, basename='add-to-cart')
router.register('order', OrderViewSet, basename='order')
router.register('seller-review', SellerReviewViewSet, basename='seller-review')
router.register('seller-review-reply', SellerReviewReplyViewSet, basename='seller-review-reply')
router.register('product-review', SellerProductReviewViewSet, basename='product-review')
router.register('product-review-reply', SellerProductReviewReplyViewSet, basename='product-review-reply')

urlpatterns = [
    path('', include(router.urls))
]
