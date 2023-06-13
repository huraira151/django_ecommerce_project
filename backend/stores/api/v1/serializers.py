from rest_framework import serializers
from users.api.v1.serializers import UserSerializer, SellerSerializer
from stores.models import Category, Product, Cart, CartItem, Order, \
    OrderItems, SellerReview, SellerReviewReply, SellerProductReview, SellerProductReviewReply
from django.db import transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# ------------
# Cart Section
# ------------

class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductCreateSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cart_items = CartItemSerializer(many=True, read_only=True, source='items_in_cart')

    class Meta:
        model = Cart
        fields = '__all__'


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']
        extra_kwargs = {"cart": {"read_only": True}}

    def create(self, validated_data):
        with transaction.atomic():
            cart_id = Cart.objects.get_or_create(user=self.context['request'].user)[0].id
            product = validated_data.get('product')
            quantity = validated_data.get('quantity')

            cart_item, created = CartItem.objects.get_or_create(
                cart_id=cart_id,
                product_id=product.id)

            cart_item.quantity = quantity
            cart_item.save()

            return cart_item

# -------------------
# End of Cart Section
# -------------------


# -------------
# Order Section
# -------------
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    products = ProductCreateSerializer()

    class Meta:
        model = OrderItems
        fields = '__all__'

# --------------------
# End of Order Section
# --------------------


# -------------------------------
# Seller Review and Reply Section
# -------------------------------
class SellerReviewReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerReviewReply
        fields = ['id', 'user', 'seller_review', 'comment']


class SellerReviewSerializer(serializers.ModelSerializer):
    review_reply = SellerReviewReplySerializer(many=True, read_only=True, source='replied_seller_review')

    class Meta:
        model = SellerReview
        fields = ['id', 'user', 'seller', 'stars', 'comment', 'review_reply']

# --------------------------------------
# End of Seller Review and Reply Section
# --------------------------------------


# --------------------------------------------------
# Product Review Create and Listing Serializers Section
# --------------------------------------------------
class SellerProductReviewReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProductReviewReply
        fields = ['id', 'user', 'seller_review', 'comment']


class SellerProductReviewSerializer(serializers.ModelSerializer):
    review_reply = SellerProductReviewReplySerializer(many=True, read_only=True, source='replied_seller_review')

    class Meta:
        model = SellerProductReview
        fields = ['id', 'user', 'seller_product', 'stars', 'comment', 'review_reply']

# ------------------------------------------------------------
# End of Product Review Create and Listing Serializers Section
# ------------------------------------------------------------


# --------------------------------
# Product Review and Reply Section
# --------------------------------
class ProductReviewReplyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProductReviewReply
        fields = ['id', 'user', 'comment']


class ProductReviewSerializer(serializers.ModelSerializer):
    review_reply = ProductReviewReplyListSerializer(many=True, read_only=True, source='replied_seller_review')

    class Meta:
        model = SellerProductReview
        fields = ['id', 'user', 'stars', 'comment', 'review_reply']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    seller = SellerSerializer()
    product_review = ProductReviewSerializer(many=True, read_only=True, source='reviewed_product')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'seller', 'category', 'product_review']

# ---------------------------------------
# End of Product Review and Reply Section
# ---------------------------------------
