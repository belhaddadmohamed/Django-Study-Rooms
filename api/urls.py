from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('room/<int:pk>/', views.getRoom),
    path('create-room/', views.createRoom),
    path('update-room/<int:pk>/', views.updateRoom),
    path('delete-room/<int:pk>/', views.deleteRoom),

    path('topics/', views.getTopics),
    path('messages/', views.getMessages),
]