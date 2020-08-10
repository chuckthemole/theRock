from django.urls import path, include
from rock.views import sport  #import everything from views module
app_name = 'rock'

urlpatterns = [
    # sport
    path('sport/publish', sport.publish_create_sport, name='publish_create_sport'),
    path('sport/create', sport.create_sport, name='create_sport'),
]
