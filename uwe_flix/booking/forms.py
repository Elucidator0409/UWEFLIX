from django import forms
from .models import Booking,Seat


class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ('seat_name',)



class SelectedSeatForm(forms.Form):
    selected_seat = forms.CharField(required=True,max_length=10,help_text='Seat No seperated by ,')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('payment_type',)
