from django.contrib.auth.models import User
from rest_framework import serializers
from .models import URL_list

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id',]


class URLlistSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()

    class Meta:
        model = URL_list
        fields = ['user_id', 'name', 'data', 'URL_long',]