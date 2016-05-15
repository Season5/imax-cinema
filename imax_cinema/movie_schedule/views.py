import string

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

import simplejson

from .custom import chunks
from .forms import TicketForm
from .models import Movie, MoviePricing, MovieViewing, Ticket, CinemaSeat
# Create your views here.
def home(request):
	movie_queryset = Movie.objects.all()
	length = len(movie_queryset)
	if length > 6:
		movie_queryset = movie_queryset[length -6:]
	print ".all: ",movie_queryset
	print ".values: ",Movie.objects.values()
	context = {
		"movies": movie_queryset,
	}
	return render(request, "index.html", context)

def about(request):
	return render(request, "about.html")

def schedule(request):
	schedule_queryset = MoviePricing.objects.all()
	context = {
		'schedule': schedule_queryset,
	}
	return render(request, "schedule.html", context)

def movie(request, id = None):
	single_movie = get_object_or_404(Movie, id = id)
	viewset = MovieViewing.objects.get(movie=single_movie)
	pricing = MoviePricing.objects.all()
	cinema_seats = CinemaSeat.objects.all()
	
	if request.session.get('seats'):
		seating = CinemaSeat.objects.filter(seat__in=request.session.get('seats')).values('id')
		print "Tiko, ", list( [seat['id'] for seat in seating ])
	
	form = TicketForm(data = request.POST)
	if form.is_valid():
		print "Valid form"
		# instance = form.save(commit=False)
		# instance.user = request.user
		# instance.seats = seating
		# instance.movie = single_movie
		reg = form.cleaned_data.get('number_of_regular_tickets')
		stu = form.cleaned_data.get('number_of_student_tickets')
		prices = form.cleaned_data.get('pricing')
		print prices
		# prices = MoviePricing.objects.get()
		payment = (reg * prices.regular_fee) + (stu * prices.student_fee)
		ticket = Ticket.objects.create(
			user= request.user,
			movie=single_movie,
			number_of_regular_tickets=reg,
			number_of_student_tickets=stu,
			pricing=prices,
			total_payment=payment)
		ticket.save()
		ticket.seat.set( list( [seat['id'] for seat in seating ]))
		# instance.save()
		# form.save_m2m()
		return redirect('movie', id)
	else:
		print[(field.label, field.errors) for field in form]
		form = TicketForm()
	context = {
		"movie": single_movie,
		"viewset": viewset,
		'seats': list(chunks(cinema_seats, 18)),
		'form': form,
		'pricing': pricing,
	}
	return render(request, "movie.html", context)
	
def seat_values(request):
	if request.is_ajax():
		seats = request.POST.getlist('seats[]')
		request.session['seats'] = seats
		response = {
			'seats': seats,
		}
		json = simplejson.dumps(response)
		return HttpResponse(json, content_type="application/json")
		