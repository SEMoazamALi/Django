from rest_framework import serializers
from .models import Account, Post

class AuthenticateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

class UnAuthenticateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'