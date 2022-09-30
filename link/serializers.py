from django.contrib.auth.models import User
from rest_framework import serializers
from .models import URL_list


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ('username',)


class URLlistSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    URL_short = serializers.URLField(read_only=True)
    data = serializers.DateTimeField(read_only=True)

    class Meta:
        model = URL_list
        fields = ('user', 'name', 'URL_long', 'URL_short', 'data', )

