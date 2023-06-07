from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.linkedin.views import LinkedInOAuthAdapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.shortcuts import get_object_or_404
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.permissions import AllowAny
from allauth.socialaccount.models import SocialAccount
from users.api.v1.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .serializers import RestSocialLoginSerializer
from rest_framework.viewsets import ViewSet
from social_login.models import *
import stripe


class LinkedinLogin(SocialLoginView):
    adapter_class = LinkedInOAuthAdapter
    client_class = OAuth2Client


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    permission_classes = [AllowAny, ]

    def get_response(self):
        user = self.request.user
        serializer_class = self.get_response_serializer()
        user_extra_data = SocialAccount.objects.filter(user=user, provider__contains='facebook').first().extra_data
        name = user_extra_data["name"]

        # Code to check if user doesn't contain name or email update the User profile
        if not user.email or not user.name:
            User.objects.filter(id=user.id).update(email=user_extra_data['email'], name=user_extra_data['name'])
            user.refresh_from_db()

        # Generate and assign stripe customer id to User
        if user.stripe_customer_id is None:
            customer = stripe.Customer.create(
                description='Customer for {}'.format(user.email),
                email=user.email
            )
            user.stripe_customer_id = customer.id
            user.save()

        user_detail = UserSerializer(user, many=False)
        resp = serializer_class(instance=self.token, context={'request': self.request}).data
        resp["token"] = resp.pop("key")
        resp["user"] = user_detail.data
        response = Response(resp, status=status.HTTP_200_OK)
        return response


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    permission_classes = [AllowAny, ]
    callback_url = "https://developers.google.com/oauthplayground"

    def get_response(self):
        serializer_class = self.get_response_serializer()
        user = self.user
        # if user.stripe_customer_id is None:
        #     customer = stripe.Customer.create(
        #         description='Customer for {}'.format(user.email),
        #         email=user.email
        #     )
        #     stripe_id = customer.stripe_id
        #     user.stripe_customer_id = stripe_id
        #     user.save()
        user_extra_data = SocialAccount.objects.filter(user=self.request.user, provider__contains='google').first().extra_data
        name = user_extra_data["name"]
        user_detail = UserSerializer(user, many=False, context={"request": self.request})
        serializer = serializer_class(instance=self.token, context={'request': self.request})
        resp = serializer.data
        resp["token"] = resp["key"]
        resp.pop("key")
        resp["user"] = user_detail.data
        # user_subscriptions = stripe.Subscription.list(customer=user.stripe_customer_id, limit=3, status='active')
        # subscription_info = user_subscriptions.get('data')
        # if subscription_info:
        #     pass
        # elif not subscription_info and StorageAllowed.objects.filter(user=user):
        #     user_subscriptions = FREE_SUBSCRIPTION_INFO
        # resp["user_subscriptions"] = user_subscriptions
        response = Response(resp, status=status.HTTP_200_OK)
        return response


# class AppleLogin(SocialLoginView):
#     authentication_classes = []
#     permission_classes = [AllowAny]
#     adapter_class = AppleOAuth2Adapter
#     serializer_class = RestSocialLoginSerializer
#
#     def get_response(self):
#         serializer_class = self.get_response_serializer()
#         user = self.user
#         user_detail = UserSerializer(user, many=False)
#         serializer = serializer_class(instance=self.token, context={'request': self.request})
#         # if user.stripe_customer_id is None:
#         #     stripe_customer = stripe.Customer.create(
#         #         description="Customer for {}".format(user.email),
#         #         email=user.email
#         #     )
#         #     user.stripe_customer_id = stripe_customer.stripe_id
#         #     user.save()
#         # user_subscriptions = stripe.Subscription.list(customer=user.stripe_customer_id, limit=3)
#         resp = serializer.data
#         resp["user"] = user_detail.data
#         resp["token"] = resp["key"]
#         # subscription_info = user_subscriptions.get('data')
#         # if subscription_info:
#         #     pass
#         # elif not subscription_info and StorageAllowed.objects.filter(user=user):
#         #     user_subscriptions = FREE_SUBSCRIPTION_INFO
#         # resp["user_subscriptions"] = user_subscriptions
#         response = Response(resp, status=status.HTTP_200_OK)
#         return response


class EmailVerificationViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def verify_user_email(self, request):
        token = request.data.get('token')
        email = request.data.get('email')

        try:
            data = VerifyEmail.objects.get(user__email=email, token=token)
            data.delete()
            return Response("Email Confirmed", status=status.HTTP_200_OK)
        except VerifyEmail.DoesNotExist:
            return Response("Invalid Token", status=status.HTTP_404_NOT_FOUND)
