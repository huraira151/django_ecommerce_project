from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import Seller
from rest_auth.serializers import LoginSerializer

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'image', 'name', 'email', 'phone_number', 'role', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'error': "Password didn't matched"})
        return attrs

    def create(self, validated_data):
        user = User(
            image=validated_data.get('image'),
            name=validated_data.get('name'),
            email=validated_data.get('email'),
            phone_number=validated_data.get('phone_number'),
            role=validated_data.get('role'),
        )

        user.set_password(validated_data.get('password'))
        user.save()

        if user.role == 'seller':
            Seller.objects.create(user=user,
                                  profile_pic=user.image,
                                  name=user.name,
                                  email=user.email,
                                  phone_number=user.phone_number)
        return user


class UserLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=False, read_only=True)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'image', 'name', 'email', 'phone_number', 'role']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
