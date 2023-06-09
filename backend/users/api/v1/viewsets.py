from rest_framework import viewsets
from .serializers import UserSignUpSerializer, UserLoginSerializer, UserSerializer, ResetPasswordConfirmSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django_rest_passwordreset.models import ResetPasswordToken
from django_rest_passwordreset.signals import pre_password_reset, post_password_reset
from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework import status, exceptions
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password, get_password_validators


User = get_user_model()


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = UserLoginSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class ResetPasswordConfirmView(viewsets.ModelViewSet):
    serializer_class = ResetPasswordConfirmSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        token = serializer.validated_data['token']

        # find token
        reset_password_token = ResetPasswordToken.objects.filter(key=token).first()

        # change users password (if we got to this code it means that the user is_active)
        try:
            if reset_password_token.user.eligible_for_reset():
                pre_password_reset.send(sender=self.__class__, user=reset_password_token.user)

                if check_password(password, reset_password_token.user.password):
                    return Response({"password": "The entered password is already the current password"}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    # validate the password against existing validators
                    validate_password(
                        password,
                        user=reset_password_token.user,
                        password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
                    )
                except ValidationError as e:
                    # raise a validation error for the serializer
                    raise exceptions.ValidationError({
                        'password': e.messages
                    })

                reset_password_token.user.set_password(password)
                reset_password_token.user.save()
                post_password_reset.send(sender=self.__class__, user=reset_password_token.user)

                # Delete all password reset tokens for this user
                ResetPasswordToken.objects.filter(user=reset_password_token.user).delete()

                return Response({'status': 'OK'})
        except:

            return Response({"status": "Token is expired or not exist"}, status=status.HTTP_400_BAD_REQUEST)
