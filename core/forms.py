# Import Django forms Module
from django import forms

# Import Our Model from which we want to build a form.
from core.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation

        # Method1: Here you are using all the fields in building the form.
        # fields = '__all__'

        # Method2: Here you specify the fields you want to use in building the form.
        fields = ['interval', 'duration']

        # Method3: Here you specify the fields you want to remove from the form.
        # exclude = ['room']

class UpdateReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation

        # Method1: Here you are using all the fields in building the form.
        # fields = '__all__'

        # Method2: Here you specify the fields you want to use in building the form.
        fields = ['room', 'interval', 'duration']

        # Method3: Here you specify the fields you want to remove from the form.
        # exclude = ['room']
