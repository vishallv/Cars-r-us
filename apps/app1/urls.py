from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^signup$',views.signUp),
    url(r'^login$',views.login),
    url(r'^listerLogReg$',views.listerLoginReg),
    url(r'^userLogReg$',views.userLogReg),
    url(r'^registerlister$',views.registerlister),
    url(r'^loglister$',views.loglister),
    url(r'^listdashboard$',views.listdashboard),
    url(r'^logout$',views.logout),
    url(r'^registeruser$',views.registeruser),
    url(r'^loginuser$',views.loguser),
    url(r'^userdashboard$',views.userdashboard),
    url(r'^search$',views.search),
    url(r'^bookcar/(?P<car_id>\d+)$',views.bookCar),
    url(r'^bookthiscar$',views.bookthiscar),
    url(r'^yourtrip$',views.yourTrip),
    url(r'^yourbooking/(?P<car_id>\d+)$',views.yourbooking),
    
    
    
    
    
 
    
]