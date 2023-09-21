from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'avatar', 'email', 'bio']