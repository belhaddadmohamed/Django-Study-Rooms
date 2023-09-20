from rest_framework import serializers
from base.models import Room, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name']



class RoomSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    class Meta:
        model = Room
        fields = '__all__'