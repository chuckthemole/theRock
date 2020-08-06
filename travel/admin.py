from django.contrib import admin
from .models import Traveler, Location, Destination, Review, Comment

admin.site.register(Traveler)
admin.site.register(Location)
admin.site.register(Destination)
admin.site.register(Review)
admin.site.register(Comment)
