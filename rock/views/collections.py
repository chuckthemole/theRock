from .imports import *

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

            coordinates = []
            for location in all_locations:
                coordinates.append([location.latitude, location.longitude])

            if len(all_locations) != 0:
                return render(request, "rock/index.html", {"user":user, "all_locations": all_locations,
                    "coordinates": coordinates, "location": all_locations[0]})
            else:
                return render(request, "rock/index.html", {"user":user, "all_locations": all_locations})
        else:
            #return render(request, "rock/login.html", {"login_dash":login_dash})
            return redirect("collections:login")
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
    print('********************************************')

    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("collections:login")
        else:
            try:
                my_locations = Location.objects.filter(rocker=user.rocker.id)
            except:
                return redirect("collections:login")

            print('*********** Testing objs retrieved from DB ************')
            #print('my_problems:', my_problems)
            #print('my_scripts:', my_scripts)
            print('*******************************************************')

            return render(request, "rock/dashboard.html", {"user":user, "my_locations":my_locations})

def create(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_base_visible = False
        all_locations = Location.objects.all()   # all_problems is a list object [   ]

        #rocker_yet = request.POST['rocker_yet']

        if username is not None and email is not None and password is not None: # checking that they are not None
            if not username or not email or not password: # checking that they are not empty
                return render(request, "rock/signup.html", {"error": "Please fill in all required fields", "is_base_visible":is_base_visible})
            if User.objects.filter(username=username).exists():
                return render(request, "rock/signup.html", {"error": "Username already exists", "is_base_visible":is_base_visible})
            elif User.objects.filter(email=email).exists():
                return render(request, "rock/signup.html", {"error": "Email already exists", "is_base_visible":is_base_visible})
            # save our new user in the User model
            user = User.objects.create_user(username, email, password)
            rocker_user = rocker.objects.create(user= user).save()
            user.save()

            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            # this logs in our new user, backend means that we are using the  Django specific auhentication and not 3rd party

        return redirect("collections:index")

    else:
        return redirect("collections:signup")

def signup(request):
    if request.user.is_authenticated:
        return redirect("collections:index")
    else:
        is_base_visible = False
        return render(request, 'rock/signup.html', {'is_base_visible':is_base_visible})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        all_locations = Location.objects.all()   # all_problems is a list object [   ]
        is_base_visible = False
        if not username or not password:
            return render(request, "rock/login.html", {"error":"One of the fields was empty", "is_base_visible":is_base_visible, "all_locations":all_locations})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("collections:index")
        else:
            return render(request, "rock/login.html", {"error":"Wrong username or password", "all_locations":all_locations, "is_base_visible":is_base_visible})
    else:
        return redirect("collections:index")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("collections:index")
    else:
        is_base_visible = False

        all_locations = Location.objects.all()   # all_problems is a list object [   ]
        coordinates = []
        for location in all_locations:
            coordinates.append([location.latitude, location.longitude])
        if len(all_locations) != 0:
            return render(request, "rock/login.html", {"all_locations": all_locations,
                "coordinates": coordinates, 'is_base_visible':is_base_visible, "location": all_locations[0]})
        else:
            return render(request, "rock/login.html", {"all_locations": all_locations, 'is_base_visible':is_base_visible})

        return render(request, 'rock/login.html', {'is_base_visible':is_base_visible})

def logout_view(request):
    logout(request)
    return redirect("collections:login")
