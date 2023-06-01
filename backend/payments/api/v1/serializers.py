from rest_framework import serializers


class CheckoutSerializer(serializers.Serializer):
    shipping_address = serializers.CharField(max_length=100, required=False)
    billing_address = serializers.CharField(max_length=100, required=False)


class CardSerializer(serializers.Serializer):
    card_holder_name = serializers.CharField(required=True)
    card_number = serializers.CharField(required=True)
    card_exp_month = serializers.CharField(required=True)
    card_exp_year = serializers.CharField(required=True)
    card_cvv = serializers.CharField(required=True)
