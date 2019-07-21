from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from chat import serializers
from chat.models import Chat
from chat.models import Room
from djoser.urls.base import User


class RoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})


class ChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = serializers.ChatSerializer(chat, many=True)

        return Response({'data': serializer.data})

    def post(self, request):
        # room = request.POST.get('room')
        status = 400
        dialog = serializers.ChatPostSerializer(data=request.POST)
        if dialog.is_valid():
            dialog.save(user=request.user)
            status = 201
        return Response(status=status)


class AddUsers(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data.get('user')
        room = Room.objects.filter(pk=request.data.get('room')).first()
        status = 400
        if room and user:
            room.visitors.add(user)
            room.save()
            status = 201
        return Response({}, status=status)
