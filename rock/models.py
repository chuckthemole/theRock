from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class rocker(models.Model):
	def __str__(self):
		return self.user.username

	rocker_yet = models.BooleanField(default=False)  # the user is not a coder yet
	local = models.BooleanField(default=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created = models.DateField(auto_now=True)   # maybe redundant, user model has date_joined :)
	updated = models.DateField(auto_now=True)

class Sport(models.Model):
	def __str__(self):
		return sport

	# FK
	rocker = models.ForeignKey(rocker, on_delete=models.CASCADE, null=True)

	sport = models.TextField(max_length=30, null=False, blank=False, unique=False)
	is_basketball = models.BooleanField(default=False)
	is_tennis = models.BooleanField(default=False)
	is_baseball = models.BooleanField(default=False)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

class Location(models.Model):
	def __str__(self):
		return (self.address + " " + self.zip)
	def num_of_destinations(self):
		destinations = Destination.objects.filter(location=self)
		return len(destinations)

	# FK
	rocker = models.ForeignKey(rocker, on_delete=models.CASCADE, null=True)

	# Sport type
	sport = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	is_basketball = models.BooleanField(default=False)
	is_tennis = models.BooleanField(default=False)
	is_baseball = models.BooleanField(default=False)

	# Location
	zip = models.TextField(max_length=5, null=False, blank=False, unique=False, default="")
	address = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	longitude = models.FloatField(null=True, blank=True, default=None)
	latitude = models.FloatField(null=True, blank=True, default=None)

	# Image of location
	sport_location_img = models.ImageField(upload_to='images/', blank=True)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)     # everytime the obj is saved, new time is saved
	#is_my_location = models.BooleanField(default=False)
	#is_visiting = models.BooleanField(default=False)

class Sport_Location(models.Model):
	def __str__(self):
		return (self.address + self.zip)

	# FK
	rocker = models.ForeignKey(rocker, on_delete=models.CASCADE, null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

	sport_location_img = models.ImageField(upload_to='images/')

class Destination(models.Model):
	def __str__(self):
		return self.title

	#FK
	rocker = models.ForeignKey(rocker, on_delete=models.CASCADE, null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

	address = models.TextField(max_length=30, null=False, blank=False, unique=False)
	zip_code = models.TextField(max_length=10, null=False, blank=False, unique=False)
	title = models.TextField(max_length=30, null=False, blank=False, unique=False)
	description = models.TextField(max_length=30, null=False, blank=False, unique=False)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

class Review(models.Model):
	def __str__(self):
		return self.title

	#FK
	destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True)
	rocker = models.ForeignKey(rocker, on_delete=models.CASCADE, null=True)

	title = models.TextField(max_length=30, null=False, blank=False, unique=False)
	stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	feedback = models.TextField(max_length=200, unique=False, blank=True)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

	class Meta:
		unique_together = (('rocker', 'destination'),)

class Comment(models.Model):
	def __str__(self):
		return self.body
	# FK
	rocker = models.ForeignKey(rocker, on_delete=models.CASCADE, null=True)
	review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)

	body = models.TextField(max_length=100, null=False, blank=False, unique=False)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)
