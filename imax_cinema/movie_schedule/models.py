from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
def upload_location(instance, filename):
	return "%s%s"%(instance.id, filename)

class Movie(models.Model):
	title = models.CharField(max_length=50)
	preview = models.ImageField(
		upload_to = upload_location, 
		null=True, 
		blank=True,
		width_field="width_field",
		height_field="height_field"
		)

	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse("movie", kwargs={'id': self.id})

class MoviePricing(models.Model):
	movie = models.ManyToManyField(Movie)
	starting_time = models.TimeField()
	student_fee = models.IntegerField(null=True, blank=True)
	regular_fee = models.IntegerField()
	def __unicode__(self):
		return str(self.starting_time)

class MovieViewing(models.Model):
	movie = models.OneToOneField(
		'Movie',
		on_delete=models.CASCADE,
		)
	movie_preview_video = models.URLField()
	movie_preview_poster = models.FileField(upload_to=upload_location)

	def __unicode__(self):
		return str(self.movie)