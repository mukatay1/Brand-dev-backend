from djoser.serializers import UserCreateSerializer as BaseCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile

User = get_user_model()


class UserCreateSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'name',
            'password'
        )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'user',
            'phone'
        )
