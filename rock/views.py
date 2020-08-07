from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Import all the models created so far
from .models import rocker, Sport, Location, Destination, Review, Comment

# import User model
from django.contrib.auth.models import User

def index(request):
    # Testing http request object inside a view function
    print('*********** Testing request obj ************')
    print('request:' , request)
    print('request.headers: ', request.headers)
    print('request.headers["host"]:', request.headers['host'])
    print('request.method: ', request.method)
    print('request.user:' , request.user)
    print('*******************************')

    if request.method == "GET":
        if request.user.is_authenticated:
            user = request.user
            all_locations = Location.objects.all()   # all_problems is a list object [   ]

            return render(request, "rock/index.html", {"user":user, "all_locations": all_locations})
        else:
            return redirect("rock:login")
    else:
        return HttpResponse(status=500)

def dashboard(request):
    # retieve user, my_problems, my-scripts
    # builds my_problems_scripts dict
    # renders dashboard.html
    # each problem should have a link show more details of a particular problem,
    # this link starts route show_my_problem

    # Testing http request object inside a view function
    print('*********** Testing request obj ************')
    print('request:' , request)
    print('request.headers: ', request.headers)
    print('request.headers["host"]:', request.headers['host'])
    print('request.method: ', request.method)
    print('request.user:' , request.user)
    print('*******************************')

    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            my_locations = Location.objects.filter(rocker=user.rocker.id)
            #my_problems = Problem.objects.filter(coder=user.coder.id)   # Problem table has a coder field (FK)
            #my_scripts =  Script.objects.filter(coder=user.coder.id)

            my_locations = Location.objects.filter(rocker=user.rocker.id)   # Problem table has a coder field (FK)

            print('*********** Testing objs retrieved from DB ************')
            #print('my_problems:', my_problems)
            #print('my_scripts:', my_scripts)
            print('*******************************')

#<<<<<<< HEAD
            return render(request, "rock/dashboard.html", {"user":user, "my_locations": my_locations})
#=======
            return render(request, "rock/dashboard.html", {"user":user, "my_locations":my_locations})

def create(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rocker_yet = request.POST['rocker_yet']

        if username is not None and email is not None and password is not None: # checking that they are not None
            if not username or not email or not password: # checking that they are not empty
                return render(request, "rock/signup.html", {"error": "Please fill in all required fields"})
            if User.objects.filter(username=username).exists():
                return render(request, "rock/signup.html", {"error": "Username already exists"})
            elif User.objects.filter(email=email).exists():
                return render(request, "rock/signup.html", {"error": "Email already exists"})
            # save our new user in the User model
            user = User.objects.create_user(username, email, password)
            rocker = rocker.objects.create(user= user, rocker_yet = rocker_yet).save()
            user.save()

            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            # this logs in our new user, backend means that we are using the  Django specific auhentication and not 3rd party

        return redirect("rock:index")

    else:
        return redirect("rock:signup")

def signup(request):
    if request.user.is_authenticated:
        return redirect("rock:index")
    return render(request, 'rock/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not username or not password:
            return render(request, "rock/login.html", {"error":"One of the fields was empty"})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("rock:index")
        else:
            return render(request, "rock/login.html", {"error":"Wrong username or password"})
    else:
        return redirect("rock:index")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("rock:index")
    return render(request, 'rock/login.html')

def logout_view(request):
    logout(request)
    return redirect("rock:login")

# Destinations
def publish_destination(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            location = get_object_or_404(Location, pk=location_id)
            return render(request, "rock/create_destination.html", {"user":user, "location":location} )

def create_destination(request, location_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        location = get_object_or_404(Location, pk=location_id)

        if not request.POST["title"]:
            return render(request, "rock/create_destination.html", {"user":user, "location":location, "error":"Please fill in all required fields"})
        else:
            #rocker, Location, address, zip, title, description
            rocker = user.rocker
            address = request.POST["address"]
            zip_code = request.POST["zip_code"]
            title = request.POST["title"]
            description = request.POST["description"]

        #if not zip_code and not title and not description:
        #    return render(request, "rock/create_destination.html", {"user":user, "location":location, "error":"Please fill in all required fields"})

        try:
            destination = Destination.objects.create(rocker=rocker, location=location, address=address, zip_code=zip_code, title=title, description=description)
            destination.save()
            destination = get_object_or_404(Destination, pk=destination.id)
            location = get_object_or_404(Location, pk=location_id)
            reviews = Review.objects.filter(destination=destination.id)
            return render(request, "rock/show_destination.html", {"rocker":rocker, "user":user, "location":location, "destination": destination, "reviews": reviews})

        except:
            return render(request, "rock/create_destination.html", {"error":"Can't create the destination"})

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
            return render(request, "rock/show_destination.html", {"user":user, "destination":destination, "reviews":reviews})

def edit_destination(request, destination_id):
    pass

def update_destination(request, destination_id):
    pass

def delete_destination(request, destination_id):
    pass

# Locations
def publish_location(request, sport_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            sport = get_object_or_404(Sport, pk=sport_id)
            return render(request, "rock/create_location.html", {"user":user, "sport":sport} )

def publish_choose_sport(request):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            return render(request, "rock/choose_sport.html", {"user":user} )

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
            return render(request, "rock/choose_sport.html", {"error":"Please fill in all required fields"})

        try:
            sport = Sport.objects.create(rocker=rocker, sport=choice, is_basketball=is_basketball, is_tennis=is_tennis, is_baseball=is_baseball)
            sport.save()
            sport = get_object_or_404(Sport, pk=sport.id)
            location = Location.objects.filter(sport=sport.id)
            return render(request, "rock/show_sport.html",{"user":user, "sport":sport})
        except:
            return render(request, "rock/choose_sport.html", {"error":"Choose a sport!"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})

def create_location(request, sport_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        sport = get_object_or_404(Sport, pk=sport_id)
        rocker = user.rocker
        address = request.POST["address"]
        zip = request.POST["zip"]

        if not address and not zip:
            return render(request, "rock/create_location.html", {"error":"Please fill in all required fields"})

        try:
            location = Location.objects.create(rocker=rocker, address=address, zip=zip, sport=sport)
            location.save()
            location = get_object_or_404(Location, pk=location.id)
            destination = Destination.objects.filter(location=location.id)


            # TODO: move this token to Django settings from an environment variable
            # found in the Mapbox account settings and getting started instructions
            # see https://www.mapbox.com/account/ under the "Access tokens" section
            mapbox_access_token = 'pk.eyJ1IjoiY2h1Y2t0aGVtb2xlIiwiYSI6ImNrZGt1cWc4NTA0MXYyc2tiaDF0Z3I4aXYifQ.CcukNwNDYUffFZtAqk3Wsg';
            return render(request, "rock/show_map.html", {"mapbox_access_token": mapbox_access_token, "user":user, "address":address, "zip": zip, "sport":sport})

        except:
            return render(request, "rock/create_location.html", {"error":"Can't create the location"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})

def show_map(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            review = get_object_or_404(Review, pk=review_id)
            comments = Comment.objects.filter(review=review_id)
            return render(request, "rock/show_comment.html", {"user":user, "review":review, "comments":comments})



def show_location(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            location = get_object_or_404(Location, pk=location_id)
            destinations = Destination.objects.filter(location=location_id)

            return render(request, "rock/show_location.html", {"user":user, "location":location, "destinations":destinations})

def edit_location(request, location_id):
   if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("share:login")

        location = get_object_or_404(Location, pk=location_id)
        # destinations = Destination.objects.filter(location=location_id)

        if location.rocker.user.id == location.rocker.user.id:
            return render(request, "rock/edit_location.html", {"location":location})
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
            return render(request, "rock/edit_location.html", {"location":location,
            "error":"One of the required fields was empty"})

        else:
            country = request.POST["country"]
            city  = request.POST["city"]

            if location.rocker.user.id == user.id:
                Location.objects.filter(pk=location_id).update(country=country,city=city)
                return redirect("rock:dashboard")

            else:
                return render(request, "rock/edit_location.html",{"location":location, "error":"Can't update!"})

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

# Reviews
def publish_review(request, destination_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            destination = get_object_or_404(Destination, pk=destination_id)
            return render(request, "rock/create_review.html", {"user":user, "destination":destination} )

def create_review(request, destination_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        destination = get_object_or_404(Destination, pk=destination_id)

        if not request.POST["title"] and not request.POST["feedback"]:
            return render(request, "rock/create_review.html", {"user":user, "destination":destination, "error":"Please fill in all required fields"})
        else:
            rocker = user.rocker
            title = request.POST["title"]
            feedback = request.POST["feedback"]
            stars = request.POST["stars"]

        try:
            review = Review.objects.create(rocker=rocker, destination=destination, feedback=feedback, title=title, stars=stars)
            review.save()
            review = get_object_or_404(Review, pk=review.id)
            destination = get_object_or_404(Destination, pk=destination.id)
            comments = Comment.objects.filter(review=review.id)
            return render(request, "rock/show_review.html", {"rocker":rocker, "user":user, "destination": destination, "review": review, "comments": comments})

        except:
            return render(request, "rock/create_review.html", {"error":"Can't create the destination"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})

def show_review(request, review_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            review = get_object_or_404(Review, pk=review_id)
            comments = Comment.objects.filter(review=review_id)

            return render(request, "rock/show_review.html", {"user":user, "review":review, "comments":comments})

def edit_review(request, review_id):
    pass

def update_review(request, review_id):
    pass

def delete_review(request, review_id):
    pass

# Comments
def publish_comment(request, review_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            review = get_object_or_404(Review, pk=review_id)
            return render(request, "rock/create_comment.html", {"user":user, "review":review} )

def create_comment(request, review_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        review = get_object_or_404(Review, pk=review_id)

        if not request.POST["body"]:
            return render(request, "rock/create_comment.html", {"user":user, "review":review, "error":"Please fill in all required fields"})
        else:
            rocker = user.rocker
            body = request.POST["body"]

        try:
            comment = Comment.objects.create(rocker=rocker, review=review, body=body)
            comment.save()
            comments = Comment.objects.filter(review=review_id)
            destination = review.destination
            return render(request, "rock/show_review.html", {"rocker":rocker, "user":user, "destination": destination, "review": review, "comments": comments})

        except:
            return render(request, "rock/create_comment.html", {"error":"Can't create the comment"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})

def show_comment(request, review_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            review = get_object_or_404(Review, pk=review_id)
            comments = Comment.objects.filter(review=review_id)
            return render(request, "rock/show_comment.html", {"user":user, "review":review, "comments":comments})

def edit_comment(request, review_id):
    pass

def update_comment(request, review_id):
    pass

def delete_comment(request, review_id):
    pass
#=======
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        review = get_object_or_404(Review, pk=review_id)

        if not request.POST["body"]:
            return render(request, "rock/create_comment.html", {"user":user, "review":review, "error":"Please fill in all required fields"})
        else:
            rocker = user.rocker
            body = request.POST["body"]

        try:
            comment = Comment.objects.create(rocker=rocker, review=review, body=body)
            comment.save()
            comments = Comment.objects.filter(review=review_id)
            destination = review.destination
            return render(request, "rock/show_review.html", {"rocker":rocker, "user":user, "destination": destination, "review": review, "comments": comments})

        except:
            return render(request, "rock/create_comment.html", {"error":"Can't create the comment"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})
#>>>>>>> master
