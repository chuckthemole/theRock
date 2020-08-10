from .imports import *

# import User model
from django.contrib.auth.models import User

# Comments
def publish_comment(request, review_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")
        else:
            review = get_object_or_404(Review, pk=review_id)
            return render(request, "rock/comment/create_comment.html", {"user":user, "review":review} )

def create_comment(request, review_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        review = get_object_or_404(Review, pk=review_id)

        if not request.POST["body"]:
            return render(request, "rock/comment/create_comment.html", {"user":user, "review":review, "error":"Please fill in all required fields"})
        else:
            rocker = user.rocker
            body = request.POST["body"]

        try:
            comment = Comment.objects.create(rocker=rocker, review=review, body=body)
            comment.save()
            comments = Comment.objects.filter(review=review_id)
            destination = review.destination
            return render(request, "rock/review/show_review.html", {"rocker":rocker, "user":user, "destination": destination, "review": review, "comments": comments})

        except:
            return render(request, "rock/comment/create_comment.html", {"error":"Can't create the comment"})

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
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("rock:login")

        review = get_object_or_404(Review, pk=review_id)

        if not request.POST["body"]:
            return render(request, "rock/comment/create_comment.html", {"user":user, "review":review, "error":"Please fill in all required fields"})
        else:
            rocker = user.rocker
            body = request.POST["body"]

        try:
            comment = Comment.objects.create(rocker=rocker, review=review, body=body)
            comment.save()
            comments = Comment.objects.filter(review=review_id)
            destination = review.destination
            return render(request, "rock/review/show_review.html", {"rocker":rocker, "user":user, "destination": destination, "review": review, "comments": comments})

        except:
            return render(request, "rock/comment/create_comment.html", {"error":"Can't create the comment"})

    else:
        user = request.user
        all_locations = Location.objects.all()
        return render(request, "rock/index.html", {"user":user, "all_locations": all_locations, "error":"Can't create!"})
