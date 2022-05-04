from django.contrib import admin

# Register your models here.
from .models import Booking,Movie,Show,BookedSeat,Theatre,Seat

class BookingAdmin(admin.ModelAdmin):
	class Meta:
		model = Booking

admin.site.register(Booking,BookingAdmin)

class ShowAdmin(admin.ModelAdmin):
	class Meta:
		model = Show

admin.site.register(Show,ShowAdmin)

class MovieAdmin(admin.ModelAdmin):
	class Meta:
		model = Movie

admin.site.register(Movie,MovieAdmin)



class BookedSeatAdmin(admin.ModelAdmin):
	class Meta:
		model = BookedSeat

admin.site.register(BookedSeat,BookedSeatAdmin)

class TheatreAdmin(admin.ModelAdmin):
	class Meta:
		model = Theatre

admin.site.register(Theatre,TheatreAdmin)

class SeatAdmin(admin.ModelAdmin):
	class Meta:
		model = Seat
admin.site.register(Seat,SeatAdmin)