from django.shortcuts import render, redirect

# Import Messages Class to help us display flash messages on the frontend.
from django.contrib import messages

# Import the Room Model.
from core.models import Room, Reservation

# Import our built form.
from core.forms import ReservationForm

# The request parameter helps django recognize this function as a view/page. 
def index(request):
    # Sending Data to the HTML Template.
    # rooms = Room.objects.all() # Retrieves all room from database.

    # Returns only the available rooms.
    rooms = Room.objects.filter(checkout=True) # Retrieves all rooms with checkout value = True

    # Preparing the Data to be sent to the HTML
    context = {'rooms': rooms}
    return render(request, 'index.html', context)


# Exercise 1
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faq.html')

# Accepts the room ID to identify the exact room the user is reserving.
def reservation(request, room_id):
    room = Room.objects.get(id = room_id)

    if request.method == 'GET':
        reservation_form = ReservationForm()

        context = {'room': room, 'form': reservation_form}
        return render(request, "reservation.html", context)
    elif request.method == 'POST':
        # print(request.POST) # Accessing the Users submitted data.
        interval = request.POST['interval'] # Extract the interval from the POST data.
        duration = request.POST['duration'] # Extract the duration from the POST data.

        # Create reservation for the specific room.
        reservation = Reservation.objects.create(
            room = room,
            interval = interval,
            duration = duration
        )

        # Update the room checkout/availability.
        room.checkout = False
        room.save()

        messages.success(request, f'Reservation for Room with ID: {room.id} was successfull!!!')

        return redirect('index')