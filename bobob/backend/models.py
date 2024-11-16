# from django.db import models


# class User(models.Model):
#     user_id = models.IntegerField()
#     user_name = models.CharField(max_length=100)
#     user_password = models.CharField(max_length=100)


# class Room(models.Model):
#     room_id = models.IntegerField()
#     room_password = models.CharField(max_length=100)
#     room_name = models.CharField(max_length=100)
#     owner_id = models.IntegerField()
#     users = models.ManyToManyField(User, through="UserOtherRooms")


# class UserOtherRooms(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     debt = models.IntegerField()

from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    user_password = models.CharField(max_length=100)

    # class Meta:
    #     verbose_name = "пользователь"
    #     verbose_name_plural = "пользователи"

    def __str__(self):
        return self.user_name


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    room_password = models.CharField(max_length=100)
    owner_id = models.IntegerField()
    users = models.ManyToManyField(User, through="UserOtherRooms")

    def __str__(self):
        return self.room_name


class UserOtherRooms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    debt = models.IntegerField()
    # DecimalField(
    #         max_digits=10,
    #         decimal_places=2,
    #         default=0.00,

    def __str__(self):
        return f"{self.user.name} в {self.room.name}"