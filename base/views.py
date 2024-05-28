from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import RoomForm, MessageForm
from .models import Room, Message, Topic
from users.models import User



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
    room_messages = Message.objects.filter(Q(room__topic__name__icontains = search_query)|
                                           Q(user__name__icontains = search_query))[0:5]

    context = {'rooms': rooms, 'topics': topics, 'room_messages':room_messages, 'search_query': search_query}

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

        # Delete also the user from participants of this room (Firstly check if the user have another messages in this room)
        if not message.user.message_set.all():      
            message.room.participants.remove(message.user)
        
        messages.success(request, "Message was deleted successfully !!")
            
        return redirect('room', pk=message.room.id)

    context = {'object': message}

    return render(request, 'base/delete.html', context)



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


