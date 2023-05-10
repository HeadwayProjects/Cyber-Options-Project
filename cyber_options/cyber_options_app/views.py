from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about01.html")

def contact(request):
    return render(request, "contact01.html")

def course(request):
    course = Course.objects.all()
    return render(request, "course01.html", {'course':course})