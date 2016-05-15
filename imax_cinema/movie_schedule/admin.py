from django.contrib import admin
from .models import Movie, MoviePricing, MovieViewing, Ticket, CinemaSeat

# Register your models here.
admin.site.register(Movie)
admin.site.register(MoviePricing)
admin.site.register(MovieViewing)
admin.site.register(Ticket)
admin.site.register(CinemaSeat)