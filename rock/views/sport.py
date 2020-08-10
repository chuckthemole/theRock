from .imports import *

# import User model
from django.contrib.auth.models import User

def publish_create_sport(request):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            form = Sport_Location_Form(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('success')
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
            return render(request, "rock/sport/show_map.html",{"user":user, "sport":sport, "location":location})
        except:
            return render(request, "rock/sport/create_sport.html", {"error":"Choose a sport!"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})
