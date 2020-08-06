# Module 0
from django.urls import path, include
from . import views  #import everything from views module
app_name = 'travel'

urlpatterns = [
    path('',views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('create', views.create, name='create'),
    path('loguser', views.login_user, name='loguser'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),

    #Destination
    path('destination/<int:location_id>/publish', views.publish_destination, name='publish_destination'),
    path('destination/<int:location_id>/create', views.create_destination, name='create_destination'),
    path('destination/<int:destination_id>/show', views.show_destination, name='show_destination'),
    path('destination/<int:destination_id>/edit', views.edit_destination, name='edit_destination'),
    path('destination/<int:destination_id>/update', views.update_destination, name='update_destination'),
    path('destination/<int:destination_id>/delete', views.delete_destination, name='delete_destination'),

    #Location
    path('location/publish', views.publish_location, name='publish_location'),
    path('location/create', views.create_location, name='create_location'),
    path('location/<int:location_id>/show', views.show_location, name='show_location'),
    path('location/<int:location_id>/edit', views.edit_location, name='edit_location'),
    path('location/<int:location_id>/update', views.update_location, name='update_location'),
    path('location/<int:location_id>/delete', views.delete_location, name='delete_location'),

    #Review
    path('review/<int:destination_id>/publish', views.publish_review, name='publish_review'),
    path('review/<int:destination_id>/create', views.create_review, name='create_review'),
    path('review/<int:review_id>/show', views.show_review, name='show_review'),
    path('review/<int:review_id>/edit', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/update', views.update_review, name='update_review'),
    path('review/<int:review_id>/delete', views.delete_review, name='delete_review'),

    #Comment
    path('comment/<int:review_id>/publish', views.publish_comment, name='publish_comment'),
    path('comment/<int:review_id>/create', views.create_comment, name='create_comment'),
#<<<<<<< HEAD
    path('comment/<int:comment_id/show', views.show_comment, name='show_comment'),
    path('comment/<int:comment_id>/edit', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/update', views.update_comment, name='update_comment'),
    path('comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),

#=======
#>>>>>>> master
]
