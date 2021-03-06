from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

from django.forms import ModelForm
# Create your models here.

class Rider(models.Model):

    user = models.OneToOneField(User)

    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        )

    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, null=False)
    address = models.TextField('Home Address', max_length=100, null=False)
    mobileNum = models.IntegerField('Mobile Number', null=False)
    nofRides = models.IntegerField('Number of rides hitches', default=0)

    REQUIRED_FIELDS = ['email', 'mobileNum', 'address', 'gender']

    def getAddress(self):
        return self.address

    def __str__(self):
        return self.user.get_full_name()


class Ride(models.Model):

    ridedmin = models.ForeignKey(Rider)
    # home = ridedmin.getHome()
    
    PLACE_CHOICES = (
            ('Home', 'Home'),
            ('IIIT-Delhi', 'IIIT-Delhi'),
        )

    startPt = models.CharField('Starting point', choices=PLACE_CHOICES, max_length=100, null=False)
    dest = models.CharField('Destination', choices=PLACE_CHOICES, max_length=100, null=False)
    time = models.DateTimeField('Departure time', null=False)
    cap = models.IntegerField('Maximum number of people in ride', null=False)
    addInfo = models.TextField('Additional info', max_length=200, blank=True)
    ladies = models.BooleanField('Ladies only', default=False)

    currPeople = models.IntegerField('Current number of hitchhikers in ride', default=0)
    dist = models.IntegerField('Distance between starting point and destination')

    REQUIRED_FIELDS = ['ridedmin', 'startPt', 'dest', 'time', 'cap']

    def __str__(self):
        retStr = startPt + " to " + dest
        return retStr

class RiderForm(ModelForm):
    class Meta:
        model = Rider
        fields = ['user','gender','address','mobileNum']

class RideForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['startPt','dest','time','cap','addInfo','ladies']
