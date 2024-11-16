
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsRoomAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.data.keys().__contains__("room"):
            room_password = get_object_or_404(
                Room.objects.all(), pk=request.data["room"]
            ).room_password
            if request.data["room_password"] == room_password:
                return True
            else:
                return False
        else:
            return False
