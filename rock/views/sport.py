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

def publish_create_sport(request):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            return render(request, "rock/sport/create_sport.html", {"user":user} )

def create_sport(request):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        rocker = user.rocker
        choice = request.POST["sports"]

        if choice == "basketball":
            is_basketball=True
            is_tennis=False
            is_baseball=False
        elif choice == "tennis":
            is_basketball=False
            is_tennis=True
            is_baseball=False
        elif choice == "baseball":
            is_basketball=False
            is_tennis=False
            is_baseball=True
        else:
            print("no choice")

        if not choice:
            return render(request, "rock/sport/create_sport.html", {"error":"Please fill in all required fields"})

        try:
            sport = Sport.objects.create(rocker=rocker, sport=choice, is_basketball=is_basketball, is_tennis=is_tennis, is_baseball=is_baseball)
            sport.save()
            sport = get_object_or_404(Sport, pk=sport.id)
            location = Location.objects.filter(sport=sport.id)
            return render(request, "rock/sport/show_sport.html",{"user":user, "sport":sport})
        except:
            return render(request, "rock/sport/create_sport.html", {"error":"Choose a sport!"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})
