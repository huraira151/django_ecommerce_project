from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from users.models import Seller

User = get_user_model()


class SellerReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_review_user')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='reviewed_seller')
    stars = models.DecimalField(max_digits=2, decimal_places=1,
                                validators=[
                                    MinValueValidator(0.0),
                                    MaxValueValidator(5.0)]
                                )
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class SellerReviewReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_review_reply_user')
    seller_review = models.ForeignKey(SellerReview, on_delete=models.CASCADE, related_name='replied_seller_review')
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class SellerProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_review_user')
    seller_product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviewed_product')
    stars = models.DecimalField(max_digits=2, decimal_places=1,
                                validators=[
                                    MinValueValidator(0.0),
                                    MaxValueValidator(5.0)]
                                )
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class SellerProductReviewReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_review_reply_user')
    seller_review = models.ForeignKey(SellerProductReview, on_delete=models.CASCADE,
                                      related_name='replied_seller_review')
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller_product')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items_in_cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in_cart')
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=200, null=True, blank=True)
    billing_address = models.CharField(max_length=200, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.total_price}"


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items_in_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='seller_products_in_order')
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
