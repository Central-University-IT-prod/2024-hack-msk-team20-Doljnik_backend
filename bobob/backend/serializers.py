from rest_framework import serializers
from .models import User, Room, UserOtherRooms


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'user_password']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_name', 'room_password', ]


class UserOtherRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOtherRooms
        fields = ['user_id', 'room_id', 'debt']

    def create(self, validated_data):
        validated_data.pop("user_password", None)
        return super().create(validated_data)
