from backend import views
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("room", views.RoomCreateView.as_view()),
    path("room/connect", views.UserOtherRoomsCreateView.as_view()),
    path("room/<int:pk>", views.RoomRetrieveView.as_view()),
    path("user/create", views.UserCreateView.as_view()),
    path("user/<int:user_id>/rooms", views.UserRoomsView.as_view()),
    path("roommate/<int:pk>", views.UserOtherRoomsRetrieveUpdateDestroyView.as_view()),
    path("rooms/<int:room_id>/users/", views.UserOtherRoomsView.as_view()),
]
