from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from pandas import DataFrame
# Import all the models created so far
from rock.models import rocker, Sport, Location, Sport_Location, Destination, Review, Comment
from rock.forms import Sport_Location_Form
from django import forms
import googlemaps
from datetime import datetime

# import User model
from django.contrib.auth.models import User

# Locations
def publish_location(request, sport_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            sport = get_object_or_404(Sport, pk=sport_id)
            return render(request, "rock/location/create_location.html", {"user":user, "sport":sport} )

def create_location(request, sport_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        sport = get_object_or_404(Sport, pk=sport_id)
        rocker = user.rocker
        address = request.POST["address"]
        zip = request.POST["zip"]

        # Geocoding an address
        gmaps = googlemaps.Client(key='AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko')
        geocode_result = gmaps.geocode(address + " " + zip)
        df = DataFrame (geocode_result)
        loc = DataFrame (df['geometry'][0])
        latitude = float(loc['location'][0])
        longitude = float(loc['location'][1])

        if not address and not zip:
            return render(request, "rock/location/create_location.html", {"error":"Please fill in all required fields"})

        try:
            location = Location.objects.create(latitude=latitude, longitude=longitude, rocker=rocker, address=address, zip=zip, sport=sport)
            location.save()
            location = get_object_or_404(Location, pk=location.id)
            #sport_location = Sport_Location.objects.create(rocker=rocker, location=location)
            """
            # form for uploading image
            form = Sport_Location_Form(request.POST, request.FILES, instance=location)
            if form.is_valid():
                location_img = form.save()
                return render((request, 'rock/map/show_success_map.html',
                             {'sport_location' : location_img}))
            """
            return render(request, "rock/map/show_map.html",
                {"longitude":longitude, "latitude":latitude, "user":user, "address":address,
                "zip":zip, "sport":sport, "location": location, #"form": form,
                "location": location})
        except:
            return render(request, "rock/location/create_location.html", {"error":"Can't create the location"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        form = Sport_Location_Form()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})

def show_location(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            location = get_object_or_404(Location, pk=location_id)
            destinations = Destination.objects.filter(location=location_id)

            return render(request, "rock/location/show_location.html", {"user":user, "location":location, "destinations":destinations})

def edit_location(request, location_id):
   if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("share:login")

        location = get_object_or_404(Location, pk=location_id)
        # destinations = Destination.objects.filter(location=location_id)

        if location.rocker.user.id == location.rocker.user.id:
            return render(request, "rock/location/edit_location.html", {"location":location})
        else:
            return render(request, "rock/index.html",
            {"error":"You are not the author of the location that you tried to edit."})

def update_location(request, location_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return HttpResponse(status=500)

        location = get_object_or_404(Location, pk=location_id)
        # destinations = Destination.objects.filter(location=location_id)

        if not request.POST["country"] or not request.POST["city"]:
            return render(request, "rock/location/edit_location.html", {"location":location,
            "error":"One of the required fields was empty"})

        else:
            country = request.POST["country"]
            city  = request.POST["city"]

            if location.rocker.user.id == user.id:
                Location.objects.filter(pk=location_id).update(country=country,city=city)
                return redirect("rock:dashboard")

            else:
                return render(request, "rock/location/edit_location.html",{"location":location, "error":"Can't update!"})

    else:
        # the user enteing    http://127.0.0.1:8000/problem/8/update
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't update!"})

def delete_location(request, location_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return HttpResponse(status=500)

        location = get_object_or_404(Location, pk=location_id)
        # destinations = Destination.objects.filter(location=location_id)

        if location.rocker.user.id == user.id:
            Location.objects.get(pk=location_id).delete()
            return redirect("rock:dashboard")
        else:
            all_locations = Location.objects.all()
            return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't delete!"})

    else:
        return HttpResponse(status=500)
