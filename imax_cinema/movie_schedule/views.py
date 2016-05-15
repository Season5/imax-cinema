import string

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

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
	
	time = timezone.now()
	
	occupied_seats = Ticket.objects.filter(
		Q(movie__exact=single_movie)&
		Q(date__exact=time)
		)
	print occupied_seats
	
	if request.session.get('seats'):
		seating = CinemaSeat.objects.filter(seat__in=request.session.get('seats')).values('id')
	
	form = TicketForm(data = request.POST)
	if form.is_valid():
		reg = form.cleaned_data.get('number_of_regular_tickets')
		stu = form.cleaned_data.get('number_of_student_tickets')
		prices = form.cleaned_data.get('pricing')
		payment = (reg * prices.regular_fee) + (stu * prices.student_fee)
		ticket = Ticket.objects.create(
			user= request.user,
			movie=single_movie,
			date=time,
			number_of_regular_tickets=reg,
			number_of_student_tickets=stu,
			pricing=prices,
			total_payment=payment)
		ticket.save()
		ticket.seat.set(list( [seat['id'] for seat in seating ]))
		return redirect('movie', id)
	else:
		form = TicketForm()
	context = {
		"movie": single_movie,
		"viewset": viewset,
		'seats': list(chunks(cinema_seats, 18)),
		'form': form,
		'pricing': pricing,
		'occupied': occupied_seats,
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
		
def occupied_seat_val(request):
	if request.is_ajax():
		time = request.GET.get('date')
		movie_id = request.GET.get('movie_id')
		occupied_seats = Ticket.objects.filter(
			Q(movie__id__exact=movie_id)&
			Q(date__exact=time)
			)
		response = {
				'seats': list(occupied_seats.values_list('seat'))
			}
		json = simplejson.dumps(response)
		return HttpResponse(json, content_type="application/json")
	