from django.conf import settings
from django.urls import include
from django.urls import path

from chat import views


urlpatterns = [
    path('room/', views.RoomView.as_view()),
    path('chat/', views.ChatView.as_view()),
    path('users/', views.AddUsers.as_view()),
]
