from .imports import *

# Destinations
def publish_destination(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            location = get_object_or_404(Location, pk=location_id)
            return render(request, "rock/destination/create_destination.html", {"user":user, "location":location} )

def create_destination(request, location_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        location = get_object_or_404(Location, pk=location_id)

        if not request.POST["title"]:
            return render(request, "rock/destination/create_destination.html", {"user":user, "location":location, "error":"Please fill in all required fields"})
        else:
            #rocker, Location, address, zip, title, description
            rocker = user.rocker
            address = request.POST["address"]
            zip_code = request.POST["zip_code"]
            title = request.POST["title"]
            description = request.POST["description"]

        #if not zip_code and not title and not description:
        #    return render(request, "rock/destination/create_destination.html", {"user":user, "location":location, "error":"Please fill in all required fields"})

        try:
            destination = Destination.objects.create(rocker=rocker, location=location, address=address, zip_code=zip_code, title=title, description=description)
            destination.save()
            destination = get_object_or_404(Destination, pk=destination.id)
            location = get_object_or_404(Location, pk=location_id)
            reviews = Review.objects.filter(destination=destination.id)
            return render(request, "rock/destination/show_destination.html", {"rocker":rocker, "user":user, "location":location, "destination": destination, "reviews": reviews})

        except:
            return render(request, "rock/destination/create_destination.html", {"error":"Can't create the destination"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})

def show_destination(request, destination_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            destination = get_object_or_404(Destination, pk=destination_id)
            reviews = Review.objects.filter(destination=destination_id)
            return render(request, "rock/destination/show_destination.html", {"user":user, "destination":destination, "reviews":reviews})

def edit_destination(request, destination_id):
    pass

def update_destination(request, destination_id):
    pass

def delete_destination(request, destination_id):
    pass
