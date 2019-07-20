from django.contrib import admin

from chat.models import Chat
from chat.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('creator', 'invited_visitors', 'date')

    def invited_visitors(self, obj):
        return '\n'.join([user.username for user in obj.visitors.all()])


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'text', 'date')
