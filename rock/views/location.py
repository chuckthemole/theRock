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

        # Geocoding an address
        address = request.POST["address"]
        zip = request.POST["zip"]
        gmaps = googlemaps.Client(key='AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko')
        geocode_result = gmaps.geocode(address + " " + zip)
        df = DataFrame (geocode_result)
        loc = DataFrame (df['geometry'][0])

        # Sometimes the DF is missing values. Try first two if they exist
        if str(loc['location'][0]) != 'nan' and str(loc['location'][1]) != 'nan':
            latitude = float(loc['location'][0])
            longitude = float(loc['location'][1])
        else:
            latitude = float(loc['location'][2])
            longitude = float(loc['location'][3])

        print("( LATITUDE: " + str(latitude) + ", LONGITUDE: " + str(longitude) + " )")
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
            try:
                location = get_object_or_404(Location, pk=location_id)
                form = Sport_Location_Form(request.POST, request.FILES, instance=location)
            except:
                return render(request, "rock/location/show_map.html", {"error":"Error"})
            if form.is_valid():
                #form.save()
                #upload = Upload(file=location.sport_location_img)
                #upload.save()
                #location.img_url = str(upload.file.url)
                location.save()
                return render(request, "rock/location/show_location.html", {"user":user, "location":location} )
            else:
                form = Sport_Location_Form()
                return render(request, "rock/location/show_map.html", {"error":"Error"})
    else:
        if request.user.is_authenticated:
            user = request.user
            location = get_object_or_404(Location, pk=location_id)
            return render(request, "rock/location/show_location.html", {"user":user, "location":location})
        else:
            return redirect("rock:login")

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
        form = Sport_Location_Form()

        # destinations = Destination.objects.filter(location=location_id)

        if location.rocker.user.id == location.rocker.user.id:
            return render(request, "rock/location/edit_location.html", {"location":location, "form":form})
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

        if 'address' in request.POST and 'zip' in request.POST:
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
                return render(request, "rock/location/edit_location.html", {"error":"Error finding address"})
            if location.rocker.user.id == user.id:
                Location.objects.filter(pk=location_id).update(address=address, zip=zip, latitude=latitude, longitude=longitude)
                return redirect("collections:dashboard")
            else:
                return render(request, "rock/location/edit_location.html",{"location":location, "error":"Can't update!"})
        elif 'sports' in request.POST:
            sport = request.POST["sports"]
            if location.rocker.user.id == user.id:
                Location.objects.filter(pk=location_id).update(sport=sport)

                if sport == "basketball":
                    Location.objects.filter(pk=location_id).update(is_basketball=True)
                    Location.objects.filter(pk=location_id).update(is_tennis=False)
                    Location.objects.filter(pk=location_id).update(is_baseball=False)
                elif sport == "tennis":
                    Location.objects.filter(pk=location_id).update(is_basketball=False)
                    Location.objects.filter(pk=location_id).update(is_tennis=True)
                    Location.objects.filter(pk=location_id).update(is_baseball=False)
                elif sport == "baseball":
                    Location.objects.filter(pk=location_id).update(is_basketball=False)
                    Location.objects.filter(pk=location_id).update(is_tennis=False)
                    Location.objects.filter(pk=location_id).update(is_baseball=True)
                else:
                    print("no choice")

                return redirect("collections:dashboard")
            else:
                return render(request, "rock/location/edit_location.html",{"location":location, "error":"Can't update!"})

        else:
            return render(request, "rock/location/edit_location.html", {"location":location,
            "error":"One of the required fields was empty"})

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
            location.sport_location_img.delete(save=False)  # Deletes the file from AWS S3
            Location.objects.get(pk=location_id).delete()   # Deletes Location instance
            return redirect("collections:dashboard")
        else:
            all_locations = Location.objects.all()
            return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't delete!"})

    else:
        return HttpResponse(status=500)
