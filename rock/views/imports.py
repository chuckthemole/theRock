from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from pandas import DataFrame
from rock.models import * # Import all the models created so far
from rock.forms import Sport_Location_Form
from django import forms
import googlemaps
from datetime import datetime
from django.contrib.auth.models import User # import User model
from rock.static.rock.images import * # Import all images
