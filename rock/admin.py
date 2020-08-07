from django.contrib import admin
from .models import rocker, Sport, Location, Destination, Review, Comment

admin.site.register(rocker)
admin.site.register(Location)
admin.site.register(Destination)
admin.site.register(Review)
admin.site.register(Comment)
