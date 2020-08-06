from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Traveler(models.Model):
	def __str__(self):
		return self.user.username

	traveler_yet = models.BooleanField(default=False)  # the user is not a coder yet
	local = models.BooleanField(default=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created = models.DateField(auto_now=True)   # maybe redundant, user model has date_joined :)
	updated = models.DateField(auto_now=True)

class Location(models.Model):
	def __str__(self):
		return self.city
	def num_of_destinations(self):
		destinations = Destination.objects.filter(location=self)
		return len(destinations)
	#FK
	traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)

	country = models.TextField(max_length=30, null=False, blank=False, unique=False)
	city = models.TextField(max_length=30, null=False, blank=False, unique=False)
	#image = models.ImageField(upload_to='myproblems/', blank=True)
	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)     # everytime the obj is saved, new time is saved
	is_my_location = models.BooleanField(default=False)
	is_visiting = models.BooleanField(default=False)

class Destination(models.Model):
	def __str__(self):
		return self.title

	#FK
	traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)

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
	destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
	traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
	title = models.TextField(max_length=30, null=False, blank=False, unique=False)
	stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	feedback = models.TextField(max_length=200, unique=False, blank=True)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

	class Meta:
		unique_together = (('traveler', 'destination'),)

class Comment(models.Model):
	def __str__(self):
		return self.body
	# FK
	traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, null=True)
	review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)

	body = models.TextField(max_length=100, null=False, blank=False, unique=False)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)
