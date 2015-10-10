from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin

from .models import Rider, Ride
# Register your models here.

class RiderInline(admin.StackedInline):
    model = Rider
    can_delete = False
    verbose_name_plural = 'rider'

class UserAdmin(UserAdmin):
    inlines = (RiderInline, )

admin.site.unregister(User)    # necessary!
admin.site.register(User, UserAdmin)
# admin.site.register(Rider)
admin.site.register(Ride)
