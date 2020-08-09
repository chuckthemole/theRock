from django import forms
from .models import *

class Sport_Location_Form(forms.ModelForm):
    class Meta:
        model = Sport_Location
        fields = ["sport_location_img"]
        #exclude = ('rocker', 'location')
