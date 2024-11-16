from rest_framework.response import Response
from .permissions import IsRoomAdmin
from rest_framework.views import APIView
from .models import User, Room, UserOtherRooms
from rest_framework import generics, status
from .serializers import UserSerializer, RoomSerializer, UserOtherRoomsSerializer


class RoomCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomRetrieveView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UserOtherRoomsCreateView(generics.CreateAPIView):
    queryset = UserOtherRooms.objects.all()
    serializer_class = UserOtherRoomsSerializer
    permission_classes = (IsRoomAdmin,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.get("room_password", None)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserOtherRoomsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserOtherRooms.objects.all()
    serializer_class = UserOtherRoomsSerializer


class UserOtherRoomsView(APIView):
    def get(self, request, room_id):
        room_users = UserOtherRooms.objects.filter(room_id=room_id)
        serializer = UserOtherRoomsSerializer(room_users, many=True)
        return Response(serializer.data)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRoomsView(APIView):
    def get(self, request, user_id):
        users = UserOtherRooms.objects.filter(user_id=user_id).values()
        admin_users = Room.objects.filter(admin=user_id).values()
        json = {
            "admin": admin_users,
            "users": users
        }
        return Response(json)
