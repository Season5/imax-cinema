from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, MoviePricing, MovieViewing
from django.shortcuts import render, get_object_or_404, redirect

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
	print "1: ", single_movie
	viewset = MovieViewing.objects.get(movie=single_movie)
	print "2: ", viewset
	context = {
		"movie": single_movie,
		"viewset": viewset,
	}
	return render(request, "movie.html", context)