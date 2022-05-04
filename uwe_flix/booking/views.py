from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

from .forms import BookingForm,SelectedSeatForm,SeatForm
import datetime


from django.http import Http404




# Create your views here.
def home(request):
	"""the homepage view"""
	context = {}
	template = 'index.html'
	return render(request,template,context)






def movie_details(request, movie_id):
	try:
		movie_info = Movie.objects.get(pk=movie_id)
		shows = Show.objects.filter(movie=movie_id,
			date=datetime.date.today()).order_by('theatre')
		show_list = []
		show_by_theatre = []
		theatre = shows[0].theatre
		for i in range(0, len(shows)):
			if theatre != shows[i].theatre:
				theatre = shows[i].theatre
				show_list.append(show_by_theatre)
				show_by_theatre = []
			show_by_theatre.append(shows[i])

		show_list.append(show_by_theatre)

	except Movie.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'movie_details.html',
		{'movie_info': movie_info, 'show_list': show_list})

@login_required(login_url='player_login')
def show_index(request):
    data = Movie.objects.all().order_by('popularity_index')
    top_movie = Movie.objects.all().order_by('popularity_index')[:3]
    movie_list = {
        "movie_list": data
    }
    return render(request, 'movielist.html', movie_list)

@login_required(login_url='player_login')
def reserve_seat(request, show_id):
    try:
        show_info = Show.objects.get(pk=show_id)
    except Show.DoesNotExist:
        raise Http404("Page Does Not Exist.")
    form  = SeatForm()
    form2 = SelectedSeatForm()
    context = {'show_info':show_info,'form':form,'form2':form2}

    return render(request,'reserve_seat.html',context)

@login_required(login_url='player_login')
def payment_gateway(request):
    if request.POST:
        seats = request.POST.get('selected_seat')
        seat_type = request.POST.get('seat_name')
        show_id = request.POST.get('show_id')

        show = Show.objects.get(pk=show_id)
        seats = seats.split(',')
        book_seat = []
        for each in seats:
            try:
                #if seat not found in DB
                s = Seat.objects.get(seat_type=seat_type,no=each, show=show)
            except:
                #redirect to seatnotfound.html
                return redirect('home')

            if Seat.objects.filter(seat_type=seat_type,no=each,show=show):
                s = Seat(no=each,seat_type=seat_type,show=show)
                book_seat.append(s)

        form = BookingForm()

        price_rate = 1000 #Yes.
        ticket_price = price_rate * len(book_seat)

        #Creating the seat string.
        seat_str = ""
        for i in range(len(seats)):
            if i == len(seats)-1:
                seat_str += seats[i]
            else:
                seat_str += seats[i] + ','

        context = {'seats': seat_str,'seat_type':seat_type,'show':show,'form':form,'ticket_price':ticket_price}
        return render(request,'booking/payment_gateway.html',context)
    else:
        return redirect('dashboard.views.home')