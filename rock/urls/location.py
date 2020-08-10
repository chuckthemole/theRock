from django.urls import path, include
from rock.views import location
app_name = 'rock'

urlpatterns = [
    # Location
    path('location/<int:sport_id>/publish', location.publish_location, name='publish_location'),
    path('location/<int:sport_id>/create', location.create_location, name='create_location'),
    path('location/<int:location_id>/show', location.show_location, name='show_location'),
    path('location/<int:location_id>/edit', location.edit_location, name='edit_location'),
    path('location/<int:location_id>/update', location.update_location, name='update_location'),
    path('location/<int:location_id>/delete', location.delete_location, name='delete_location'),
]
