from django.shortcuts import render, render_to_response 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Needed for Google Maps API
import requests, json

from .models import Rider, Ride, RideForm
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
        if dest == 'Home':
            dest = currRider.getAddress()

        context_dict = {
                'startPt': startPt,
                'dest': dest,
            }
        return render(request, 'ridesharing/rides.html', context_dict)

    return render(request, 'ridesharing/home.html')


@login_required(login_url = '/ridesharing/login/')
def rideFormPage(request):
    
    currRider = Rider.objects.get(user = request.user)

    if request.method == 'POST':

        form = RideForm(request.POST)
        if form.is_valid():

            startPt = form.cleaned_data['startPt']
            dest = form.cleaned_data['dest']

            if startPt == 'Home':
                startPt = currRider.getAddress()
            if dest == 'Home':
                dest = currRider.getAddress()

            time = form.cleaned_data['time']
            cap = form.cleaned_data['cap']
            addInfo = form.cleaned_data['addInfo']
            ladies = form.cleaned_data['ladies']
            
            ride = Ride(
                    ridemin = currRider,
                    startPt = startPt,
                    dest = dest,
                    time = time,
                    cap = cap,
                    addInfo = addInfo,
                    ladies = ladies,
                )

            ride.save()
            # return HttpResponseRedirect('/ridesharing/home')
            return render(request, 'ridesharing/home.html')
    else:
        form = RideForm()
        return render(request, 'ridesharing/ride_form.html', {'form': form})


############## TODO #############################
def processRides(request, ride):
    if request.METHOD == 'POST':
        dist = request.POST['dist']
        ride.strip(' km')
        ride.dist = dist
        ride.save()
        return render(request, 'ridesharing/rides.html')
    else:
        context_dict = {
                'source': ride.source,
                'destination': ride.dest,
            }
        return render(request, 'ridesharing/findDist.html', context_dict)

def findDist(source, dest):
    payload = {
        'origins' : source,
        'destinations' : dest,
    }
    api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    r = requests.get(api_url, params=payload)
    parsed_json = json.loads(r.text)
    request_status = parsed_json['status']
    if request_status != 'OK':
        return None
    dist_status = parsed_json['rows'][0]['elements'][0]['status']
    if dist_status != 'OK':
        return None
    else:
        distance = parsed_json['rows'][0]['elements'][0]['distance']
        return distance['text']

@login_required(login_url = '/ridesharing/login/')
def rides(request):
    currR = Entry.objects.latest()
    rList = []
    threshold = 2
    for r in Rides.objects.all():
        processRides(request, r)
    for r in Rides.objects.all():
        if abs(r.dist - currR.dist) <= threshold:
            rList.append(r)
############## TODO #############################
    

        
