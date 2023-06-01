from django.contrib import admin
from stores.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'seller', 'price', 'name', 'description']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity', 'created_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price', 'user', 'date_ordered']


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']


class SellerReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'seller', 'stars', 'comment', 'created_at']


class SellerReviewReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'seller_review', 'comment', 'created_at']


class SellerProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'seller_product', 'stars', 'comment', 'created_at']


class SellerProductReviewReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'seller_review', 'comment', 'created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
admin.site.register(SellerReview, SellerReviewAdmin)
admin.site.register(SellerReviewReply, SellerReviewReplyAdmin)
admin.site.register(SellerProductReview, SellerProductReviewAdmin)
admin.site.register(SellerProductReviewReply, SellerProductReviewReplyAdmin)
