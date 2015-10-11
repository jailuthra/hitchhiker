from django.shortcuts import render, render_to_response 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Rider, Ride#, RiderForm, RideForm
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/ridesharing/home/')
    return render(request, 'ridesharing/login.html')


def sign_up(request):
    return None
     

@login_required(login_url = '/ridesharing/login/')
def index(request):
    return HttpResponse("Hello World!")

@login_required(login_url = '/ridesharing/login/')
def home(request):

    currRider = Rider.objects.get(user = request.user)

    if request.method == 'POST':
        startPt = request.POST['startPt']
        dest = request.POST['dest']

        if startPt == 'Home':
            startPt = currRider.getAddress()
        elif startPt == 'IIIT-Delhi':
            startPt = 'IIIT-Delhi' #give proper coordinates
        if dest == 'Home':
            dest = currRider.getAddress()
        elif dest == 'IIIT-Delhi':
            dest = 'IIIT-Delhi'

        context_dict = {
                'startPt': startPt,
                'dest': dest,
            }
        return render(request, 'ridesharing/rides.html', context_dict)

    return render(request, 'ridesharing/home.html')


@login_required(login_url = '/ridesharing/login/')
def rides(request):
    return None 
