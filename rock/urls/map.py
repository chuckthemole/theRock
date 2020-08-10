from django.urls import path, include
from rock.views import map
app_name = 'rock'

urlpatterns = [
    # Map
    path('map/<int:sport_id/show', map.show_map, name='show_map'),
    path('create', map.create_form, name='create_form'),

    path('image/<int:location_id>/publish', map.publish_image, name='publish_image'),
    path('image/<int:location_id>/create', map.create_image, name='create_image'),

    path('location_to_image/<int:location_id>/transition', map.location_to_image, name="location_to_image"),

    # Sport Location
    path('sport_location/<int:sport_id>/publish', map.publish_sport_location, name='publish_sport_location'),
    path('sport_location/<int:sport_id>/create', map.create_sport_location, name='create_sport_location'),
    path('sport_location/<int:sport_id>/show', map.show_sport_location, name='show_sport_location'),

]
