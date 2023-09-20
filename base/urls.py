from django.urls import path
from . import views


urlpatterns = [
    path('', views.rooms, name="home"),
    path('room/<int:pk>/', views.room, name="room"),
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('update-user/', views.update_user, name="update-user"),

    path('create-room/', views.create_room, name="create-room"),
    path('update-room/<int:pk>/', views.update_room, name="update-room"),
    path('delete-room/<int:pk>/', views.delete_room, name="delete-room"),

    path('delete-message/<int:pk>/', views.delete_message, name="delete-message"),

    path('topics/', views.topics, name="topics"),
    path('activities/', views.activity, name="activities"),

    path('login/', views.loginUser, name="login"),
    path('signup/', views.signupUser, name="signup"),
    path('logout/', views.logoutUser, name="logout"),

]