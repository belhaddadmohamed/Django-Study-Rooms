from rest_framework import serializers
from base.models import Room, Topic, Message
from users.models import User
from django.utils.timezone import now



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class TopicSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = '__all__'
        # fields = ['name']

    def get_rooms(self, obj):
        rooms = obj.room_set.all()
        serializer = RoomSerializer(rooms, many=True)

        return serializer.data



class RoomSerializer(serializers.ModelSerializer):
    host = UserSerializer(many=False)
    days_since_created = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_topic(self, obj):
        topic_name = obj.topic.name
        return {'name': topic_name}

    def get_days_since_created(self, obj):
        days_since = (now() - obj.created) / 3600 / 24      # Days
        return days_since



class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    room = RoomSerializer()

    class Meta:
        model = Message
        fields = '__all__'


