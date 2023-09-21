from django.urls import path
from . import views


urlpatterns = [    
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('update-user/', views.update_user, name="update-user"),
    path('login/', views.loginUser, name="login"),
    path('signup/', views.signupUser, name="signup"),
    path('logout/', views.logoutUser, name="logout"),

]