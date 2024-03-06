from django.db import models

# Create your models here.
class Room(models.Model):
    standard_choices = (
        ('Regular', 'Regular'),
        ('Executive', 'Executive'),
        ('Royal', 'Royal'),
        ('Pent-House', 'Pent-House'),
    )

    standard = models.CharField(max_length=50, choices=standard_choices)
    price = models.FloatField()
    occupants = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    checkout = models.BooleanField(default=True)

    # Changes the default name Displayed on each object on the admin panel
    def __str__(self):
        return self.standard


class Reservation(models.Model):
    interval_choices = (
        ('Hour', 'Hour'),
        ('Day', 'Day'),
        ('Week', 'Week'),
        ('Month', 'Month'),
    )
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    interval = models.CharField(max_length=20, choices=interval_choices)
    duration = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    # Exercise 2
    # Adding Extra Fields to the Reservation Model
    # fullname = models.CharField(max_length=100)
    # email = models.EmailField()
    # phone = models.CharField(max_length=15)

    # Changes the default name Displayed on each object on the admin panel
    def __str__(self):
        return self.room.standard
