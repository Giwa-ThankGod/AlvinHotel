from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name="index"),
    path('reservation/<room_id>/', views.reservation, name='reservation'),
    path('update-booking/<booking_id>/', views.update_booking, name='update-booking'),
    path('delete-booking/<booking_id>/', views.delete_booking, name='delete-booking'),
    path('bookings/', views.bookings, name="bookings")
]