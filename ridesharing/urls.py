from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    # url(r'^sign-up/$', views.sign_up, name='sign-up'),
    url(r'^home/$', views.home, name='home'),
    url(r'^rides/$', views.rides, name='rides'),
]
