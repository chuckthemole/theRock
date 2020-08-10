from .imports import *

# import User model
from django.contrib.auth.models import User

# Reviews
def publish_review(request, destination_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            destination = get_object_or_404(Destination, pk=destination_id)
            return render(request, "rock/review/create_review.html", {"user":user, "destination":destination} )

def create_review(request, destination_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        destination = get_object_or_404(Destination, pk=destination_id)

        if not request.POST["title"] and not request.POST["feedback"]:
            return render(request, "rock/review/create_review.html", {"user":user, "destination":destination, "error":"Please fill in all required fields"})
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
            return render(request, "rock/review/show_review.html", {"rocker":rocker, "user":user, "destination": destination, "review": review, "comments": comments})

        except:
            return render(request, "rock/review/create_review.html", {"error":"Can't create the destination"})

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

            return render(request, "rock/review/show_review.html", {"user":user, "review":review, "comments":comments})

def edit_review(request, review_id):
    pass

def update_review(request, review_id):
    pass

def delete_review(request, review_id):
    pass
