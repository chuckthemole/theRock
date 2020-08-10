# Module 0
from django.urls import path, include
from . import views  #import everything from views module
app_name = 'rock'

urlpatterns = [


    path('success', views.success, name = 'success'),

    # Testing
    path('test', views.test, name='test'),
]
