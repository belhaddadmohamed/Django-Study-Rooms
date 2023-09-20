from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Message
from users.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['host', 'participants']
        labels = {
            'name': 'Room name',
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'avatar', 'email', 'bio']