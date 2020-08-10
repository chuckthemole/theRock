from django.urls import path, include
from rock.views import destination  #import everything from views module
app_name = 'rock'

urlpatterns = [
    # Destination
    path('destination/<int:location_id>/publish', destination.publish_destination, name='publish_destination'),
    path('destination/<int:location_id>/create', destination.create_destination, name='create_destination'),
    path('destination/<int:destination_id>/show', destination.show_destination, name='show_destination'),
    path('destination/<int:destination_id>/edit', destination.edit_destination, name='edit_destination'),
    path('destination/<int:destination_id>/update', destination.update_destination, name='update_destination'),
    path('destination/<int:destination_id>/delete', destination.delete_destination, name='delete_destination'),
]
