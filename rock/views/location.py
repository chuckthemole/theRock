from .imports import *

# Locations
def publish_location(request):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            return render(request, "rock/location/create_location.html", {"user":user} )

def create_location(request):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        rocker = user.rocker
        sport = request.POST["sports"]

        # Choose sport
        if sport == "basketball":
            is_basketball=True
            is_tennis=False
            is_baseball=False
        elif sport == "tennis":
            is_basketball=False
            is_tennis=True
            is_baseball=False
        elif sport == "baseball":
            is_basketball=False
            is_tennis=False
            is_baseball=True
        else:
            print("no choice")

        if not sport:
            return render(request, "rock/location/create_location.html", {"error":"Please choose a sport!"})

        try:
            # Geocoding an address
            address = request.POST["address"]
            zip = request.POST["zip"]
            gmaps = googlemaps.Client(key='AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko')
            geocode_result = gmaps.geocode(address + " " + zip)
            df = DataFrame (geocode_result)
            loc = DataFrame (df['geometry'][0])
            latitude = float(loc['location'][0])
            longitude = float(loc['location'][1])
        except:
            # If address is blank or not found
            return render(request, "rock/location/create_location.html", {"error":"Error finding address"})

        # Make more requirements for adress inputs
        if address == "" or len(zip) < 5:
            return render(request, "rock/location/create_location.html", {"error":"Enter a proper address"})

        try:
            location = Location.objects.create(
                sport_location_img='images/no_image_available.PNG',
                latitude=latitude, longitude=longitude,
                rocker=rocker, address=address, zip=zip,
                sport=sport, is_basketball=is_basketball,
                is_tennis=is_tennis, is_baseball=is_baseball)
            location.save()
            location = get_object_or_404(Location, pk=location.id)
            return render(request, "rock/location/show_sport.html", {"user":user, "location":location})
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

def publish_image(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            location = get_object_or_404(Location, pk=location_id)
            form = Sport_Location_Form()
            return render(request, "rock/location/show_map.html", {"user":user, "location":location, "form":form} )

def create_image(request, location_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            location = get_object_or_404(Location, pk=location_id)
            form = Sport_Location_Form(request.POST, request.FILES, instance=location)
            if form.is_valid():
                form.save()
                return render(request, "rock/location/show_image.html", {"user":user, "location":location} )
            else:
                form = Sport_Location_Form()

def show_image(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            location = get_object_or_404(Location, pk=location_id)
            return render(request, "rock/location/show_image.html", {"user":user, "location":location})

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
            return redirect("collections:dashboard")
        else:
            all_locations = Location.objects.all()
            return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't delete!"})

    else:
        return HttpResponse(status=500)
