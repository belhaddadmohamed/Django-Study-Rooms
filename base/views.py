from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .models import Room, Message, Topic
from .forms import RoomForm, MessageForm, CustomUserCreationForm, UserForm


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist !!")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Hello "+str(user.first_name))
            return redirect(request.GET.get('next') if 'next' in request.GET else 'home')
        else:
            messages.error(request, "password or username incorrect !!")

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



def rooms(request):
    # rooms = Room.objects.all()
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    rooms = Room.objects.distinct().filter(Q(name__icontains = search_query) |
                                           Q(host__username__icontains = search_query) |
                                           Q(topic__name__icontains = search_query) |
                                           Q(description__icontains = search_query))


    topics = Topic.objects.all()[0:5]
    room_message = Message.objects.filter(Q(room__topic__name__icontains = search_query))

    context = {'rooms': rooms, 'topics': topics, 'room_messages':room_message, 'search_query': search_query}

    return render(request, 'base/index.html', context)



def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()  # it's a ManyToMany relationship

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room
            message.save()

            room.participants.add(message.user)
            
            return redirect('room', pk=room.id)
    
    context = {'room': room, 'room_messages': room_messages, 'participants':participants, 'form': form}

    return render(request, 'base/room.html', context)



@login_required(login_url='login')
def delete_message(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You're not allowed here !!")

    if request.method == 'POST':
        message.delete()

        # Delete also the user from participants of this room (check first if the user have other messages in this room)
        if not message.user.message_set.all():      
            message.room.participants.remove(message.user)
        
        messages.success(request, "Message was deleted successfully !!")
            
        return redirect('room', pk=message.room.id)

    context = {'object': message}

    return render(request, 'base/delete.html', context)


  
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
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)
    
    context = {'form': form}

    return render(request, 'base/update-user.html', context)


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()
    context = {'form': form, 'topics':topics}

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description'),  
        )
    
        messages.success(request, "Room created successfully !!")
        return redirect('home')

    return render(request, 'base/create-room.html', context)



@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    topics = Topic.objects.all()
    form = RoomForm(instance=room)

    if request.user != room.host:   
        return HttpResponse("You're not allowed here !!")

    if request.method == 'POST': 
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.topic = topic
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.save()

        messages.success(request, "Room was updated successfully !!")
        return redirect('room', pk=room.id)

    context = {'form': form, 'topics': topics, 'room':room}

    return render(request, 'base/create-room.html', context)



@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You're not allowed here !!")

    if request.method == 'POST':
        room.delete()
        messages.success(request, "Messages was deleted successfully !!")
        return redirect('home')

    context = {'object': room}

    return render(request, 'base/delete.html', context)



def topics(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    topics = Topic.objects.distinct().filter(Q(name__icontains = search_query))

    context = {'topics': topics}

    return render(request, 'base/topics.html', context)


def activity(request):
    room_messages = Message.objects.all()
    context = {'room_messages': room_messages}

    return render(request, 'base/activity.html', context)


