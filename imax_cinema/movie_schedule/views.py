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
	seats = CinemaSeat.objects.all()
	form = TicketForm()
	context = {
		"movie": single_movie,
		"viewset": viewset,
		'seats': list(chunks(seats, 18)),
		'form': form,
		'pricing': pricing,
	}
	return render(request, "movie.html", context)
	
def seat_values(request):
	if request.is_ajax():
		seats = request.POST.getlist('seats[]')
		movie_id = request.POST.getlist('id')
		form = TicketForm(request.POST)
		print "Seats: ", seats
		tickets = CinemaSeat.objects.filter(seat__in=seats)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.ticket = tickets
			instance.movie = Movie.objects.get(id=movie_id)
			instance.save()
		else:
			form = TicketForm()
		response = {
			'seats': seats,
		}
		json = simplejson.dumps(response)
		return HttpResponse(json, content_type="application/json")
		