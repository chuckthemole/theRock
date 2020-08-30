from django.urls import path, include
from rock.views import collections
app_name = 'rock'

urlpatterns = [
    path('',collections.index, name='index'),
    path('dashboard', collections.dashboard, name='dashboard'),

    path('create', collections.create, name='create'),
    path('loguser', collections.login_user, name='loguser'),
    path('login', collections.login_view, name='login'),
    path('logout', collections.logout_view, name='logout'),
    path('signup', collections.signup, name='signup'),
    path('profile_pic/<int:rocker_id>/publish', collections.publish_profile_pic, name='publish_profile_pic'),
    path('profile_pic/<int:rocker_id>/create', collections.create_profile_pic, name='create_profile_pic'),
]
