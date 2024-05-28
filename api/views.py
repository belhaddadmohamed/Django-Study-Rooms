from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Room, Topic, Message
from .serializers import RoomSerializer, TopicSerializer, MessageSerializer, UserSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = {
        "routes" : "GET api/",
        "rooms" : "GET api/rooms/",
        "room" : "GET api/room/pk",
        "create room" : "POST api/create-room/pk",
        "update room" : "POST api/update-room/pk",
        "delete room" : "DELETE api/delete-room/pk",
        "topics" : "GET api/topics/",
        "messages" : "GET api/messages/",
    }

    return Response(routes) 



@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)

    return Response(serializer.data)



@api_view(["GET"])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)

    return Response(serializer.data)



@api_view(["POST"])
def createRoom(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(data=request.data, instance=room)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()

    return Response({"messages": "Room '"+ str(room) +"' was created successfully"})



@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data)