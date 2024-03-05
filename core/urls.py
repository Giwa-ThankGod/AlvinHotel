from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name="index"),
    path('reservation/<room_id>/', views.reservation, name='reservation')
]