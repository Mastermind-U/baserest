from djoser.urls.base import User
from rest_framework import serializers

from chat.models import Chat
from chat.models import Room


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'get_full_name')


class RoomSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    visitors = UserSerializer(many=True)
    date = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M",
        required=False,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = ('pk', 'creator', 'visitors', 'date')


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    date = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M",
        required=False,
        read_only=True,
    )

    class Meta:
        model = Chat
        fields = ('user', 'text', 'date')


class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('room', 'text')
