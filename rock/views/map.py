from .imports import *

# import User model
from django.contrib.auth.models import User

def show_map():
    pass

def create_form(request, form, sport_location):
    if form.is_valid():
        form.save()
        return render((request, 'rock/map/show_success_map.html',
                     {'sport_location' : sport_location}))

def publish_image(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            location = get_object_or_404(Location, pk=location_id)
            form = Sport_Location_Form(request.POST, request.FILES, instance=location)

            return render(request, "rock/image/create_image.html", {"user": user, "location": location, "form": form} )

def create_image(request, location_id, form):
    if request.method == 'POST':
        location = get_object_or_404(Location, pk=location_id)
        form = Sport_Location_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Sport_Location_Form()
    return render(request, 'show_success_map.html', {'form' : form})

def location_to_image(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            location = get_object_or_404(Location, pk=location_id)
            return render(request, "rock/image/create_image.html",{"user":user, "location":location})

# Sport_Location
def publish_sport_location(request, sport_id):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = request.user
            all_locations = Location.objects.all()   # all_problems is a list object [   ]

            return render(request, "rock/index.html", {"user":user, "all_locations": all_locations})
        else:
            return redirect("rock:login")
    else:
        return HttpResponse(status=500)

def create_sport_location(request, sport_id):
    pass

def show_sport_location(request, sport_id):
    pass
