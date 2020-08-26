import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

class rocker(models.Model):
	def __str__(self):
		return self.user.username

	#rocker_yet = models.BooleanField(default=False)  # the user is not a coder yet
	#local = models.BooleanField(default=False)
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

class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

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
	sport_location_img = models.ImageField(upload_to='images/', blank=True, default="static/rock/images/no_image_available.PNG")
	img_url = models.TextField(max_length=100, null=False, blank=True, unique=False, default="")

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

@receiver(models.signals.post_delete, sender=Location)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.sport_location_img:
        if os.path.isfile(instance.sport_location_img.path):
            os.remove(instance.sport_location_img.path)

@receiver(models.signals.pre_save, sender=Location)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Location.objects.get(pk=instance.pk).sport_location_img
    except Location.DoesNotExist:
        return False

    new_file = instance.sport_location_img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
