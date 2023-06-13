from stores.api.v1.serializers import *
from rest_framework import viewsets, generics
from stores.models import *
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ProductCreateSerializer
        else:
            return ProductListSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class AddToCartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = {
            "product": request.data.get("product"),
            "quantity": request.data.get("quantity")
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SellerReviewViewSet(viewsets.ModelViewSet):
    queryset = SellerReview.objects.all()
    serializer_class = SellerReviewSerializer
    permission_classes = [IsAuthenticated]


class SellerReviewReplyViewSet(viewsets.ModelViewSet):
    queryset = SellerReviewReply.objects.all()
    serializer_class = SellerReviewReplySerializer
    permission_classes = [IsAuthenticated]


class SellerProductReviewViewSet(viewsets.ModelViewSet):
    queryset = SellerProductReview.objects.all()
    serializer_class = SellerProductReviewSerializer
    permission_classes = [IsAuthenticated]


class SellerProductReviewReplyViewSet(viewsets.ModelViewSet):
    queryset = SellerProductReviewReply.objects.all()
    serializer_class = SellerProductReviewReplySerializer
    permission_classes = [IsAuthenticated]
