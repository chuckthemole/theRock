# traveler_software_engineering

Group Members:
 1) Charles Thomas
 2) Omoremi Adeleke
 3) Tania Ortiz-Rosales
 4) Redeat Kibebew

Feature: Index Page
As an authenticated user of the web site traveler
So that I can determine what country and city I may want to visit next
I want a list of all the locations from the Location Table in the home page index
Route: / or index → views.index function → index.html

Feature: Dashboard page
As an authenticated user of the web site
I want to have a page dashboard.html that shows
So that  I can
Route:  /dashboard or dashboard → views.dashboard function → dashboard.html

Feature: Show a Destination
As an authenticated user of the web site traveler
I want a destination to be displayed with all of its features
So that I can see the location, interesting features, and other descriptions about a destination.
Route: show → views.show_destination → show_destination.html

<<<<<<< HEAD
Feature: Show a Review
As an authenticated user of the web site traveler
I want reviews of destinations to be displayed
So that I can see people’s suggestions
Route: show → views.show_review → show_review.html
=======
Feature: Show a Location
As an authenticated user of the website traveler
So that I can read all the possible destinations of one location
I want to list all the attributes of a particular location
Route: location/<int:location_id>/show or show_location → views.show_location function → show_location.html
>>>>>>> d4bd3fcecec0a6508aa367da3c5cbb0d06f92ec9

Feature: Create a location
As an authenticated user of the web site traveler
I want to be able to create a location to be displayed
So that I can show other users different locations I’m interested in
Route: create → views.create_location → create_location.html
Route: location/publish → views.publish_location, create_location.html
Route: location/create → views.create_location, show_location.html

Feature: Create a destination
As an authenticated user of the web site traveler
I want to be able to create a destination to be displayed
So that I can show other users different destinations I’m interested in
Route: destination/publish → views.publish_destination, create_destination.html
Route: destination/create → views.create_destination, show_destination.html


Feature: Create a review
As an authenticated user of the web site traveler
I want to be able to create a review to be displayed
So that I can let other users know how I feel about a particular destination
Route: review/publish → views.publish_review, create_review.html
Route: review/create → views.create_review, show_review.html

Feature: Create a comment
As an authenticated user of the web site traveler
I want to be able to create a comment for a review to be displayed
So that I can let other users know how I feel about a their review
Route: comment/publish → views.publish_comment, create_comment.html
Route: comment/create → views.create_comment, show_review.html

# source djangoenv/Scripts/activate
