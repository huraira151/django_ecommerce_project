from rest_framework import generics, viewsets, views, status
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
from stores.models import *
from rest_framework.permissions import IsAuthenticated
import stripe
from djstripe.models import Customer
from rest_framework.decorators import action
import json
from django.conf import settings
from django.db import transaction
from django.db.models import Sum, F

stripe.api_key = settings.STRIPE_API_KEY


class AddPaymentMethodView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        user = request.user
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        stripe_customer = Customer.get_or_create(subscriber=user)
        if stripe_customer[1]:
            user.stripe_customer_id = stripe_customer[0].id
            user.save()
        try:
            token = stripe.Token.create(
                card={
                    "name": data.get("card_holder_name"),
                    "number": data.get("card_number"),
                    "exp_month": data.get("card_exp_month"),
                    "exp_year": data.get("card_exp_year"),
                    "cvc": data.get("card_cvv")
                }, )

            card = stripe.Customer.create_source(
                user.stripe_customer_id,
                default_source=token.id,
            )

            stripe_customer[0].add_payment_method(
                payment_method=card.id, set_default=True)
        except stripe.error.CardError as e:
            return Response(e)
        return Response("Payment Method Added successfully", status=status.HTTP_201_CREATED)


class CheckoutView(generics.GenericAPIView):
    serializer_class = CheckoutSerializer

    @staticmethod
    def post(request):
        with transaction.atomic():
            cart = get_object_or_404(Cart, user=request.user)
            cart_item = CartItem.objects.filter(cart=cart)
            cart_item_annotate = cart_item.annotate(total_price=Sum(F('product__price') * F('quantity')))\
                .values('total_price', 'product_id', 'quantity')
            new_total_price = cart_item_annotate.aggregate(total=Sum("total_price"))

            order = Order.objects.create(
                user=request.user,
                total_price=new_total_price['total'],
                shipping_address=request.data.get('shipping_address'),
                billing_address=request.data.get('billing_address')
            )

            checkout_payment = stripe.PaymentIntent.create(
                amount=int(new_total_price['total']) * 100,
                currency='usd',
                automatic_payment_methods={'enabled': True},
            )

            order_items = [
                OrderItems(order=order, product_id=item['product_id'], quantity=item['quantity'])
                for item in cart_item_annotate
            ]
            OrderItems.objects.bulk_create(order_items)

            cart.delete()
            cart_item.delete()

        return Response({'detail': 'Order created successfully'}, status=status.HTTP_200_OK)


class PaymentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def get_customer_id(self, request):
        user = request.user
        customer_id = user.stripe_customer_id

        if not customer_id:
            customer = Customer.create(subscriber=user)
            user.stripe_customer_id = customer.id
            user.save()

        response_data = {"stripe_customer_id": customer_id}
        return Response(response_data)

    @action(detail=False, methods=['delete'])
    def delete_card(self, request):
        card_id = request.data.get("card_id")
        user = self.request.user

        stripe.Customer.delete_source(user.stripe_customer_id, card_id)

        return Response("Card deleted successfully")

    @action(detail=False, methods=['get'])
    def get_all_cards(self, request):
        user = request.user
        customer = Customer.objects.filter(subscriber=user).first()

        default_card_id = customer.default_payment_method.id if customer.default_payment_method else False

        card_list = stripe.PaymentMethod.list(
            customer=user.stripe_customer_id,
            type="card"
        )

        data = {
            "list_card": card_list.data,
            "default_card_id": default_card_id
        }

        return Response(data)

    @action(detail=False, methods=['get'])
    def get_card(self, request):
        user = self.request.user
        customer = Customer.objects.filter(subscriber=user).first()

        if customer and customer.default_payment_method:
            default_payment_method = customer.default_payment_method
            card_data = json.dumps(default_payment_method.card)
            return Response(json.loads(card_data))

        return Response(None)

    @action(detail=False, methods=['post'])
    def set_card_default(self, request):
        card_id = request.data.get("card_id")
        user = request.user
        customer = Customer.objects.filter(id=user.stripe_customer_id)\
            if user.stripe_customer_id else Customer.objects.filter(subscriber=user)
        if customer.exists():
            customer = customer.first()
            customer.add_payment_method(payment_method=card_id, set_default=True)
            return Response("Successfully set card as default")
        return Response("Failed to set card as default")
