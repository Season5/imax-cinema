from django.contrib import admin
from .models import Movie, MoviePricing, MovieViewing

# Register your models here.
admin.site.register(Movie)
admin.site.register(MoviePricing)
admin.site.register(MovieViewing)