from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, UserForm
from base.models import Topic
from .models import User



def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User doesn't exist !!")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Hello "+str(user.first_name))
            return redirect(request.GET.get('next') if 'next' in request.GET else 'home')
        else:
            messages.error(request, "password or email incorrect !!")

    context = {'page': page}

    return render(request, 'base/login_register.html', context)



@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    messages.success(request, "You're logged out")
    return redirect('login')



def signupUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            messages.success(request, "Hello "+user.username)

            return redirect(request.GET.get('next') if 'next' in request.GET else 'home')

    context = {'page': page, 'form': form}

    return render(request, 'base/login_register.html', context)





def profile(request, pk):
    profile = User.objects.get(id=pk)
    rooms = profile.room_set.all()
    room_messages = profile.message_set.all()
    topics = Topic.objects.all()[0:5]

    context = {'profile': profile, 'rooms':rooms, 'topics':topics, 'room_messages': room_messages}

    return render(request, 'base/profile.html', context)



@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)
    
    context = {'form': form}

    return render(request, 'base/update-user.html', context)


