from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Profile, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'userProfile', 'created_on', 'img')
        extra_kwargs = {'userProfile': {'read_only': True}}


class PostSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'userPost', 'created_on', 'img', 'liked')
        extra_kwargs = {'userPost': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'userComment', 'post')
        extra_kwargs = {'userComment': {'read_only': True}}
