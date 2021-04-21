from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="Home"),
    path('events',views.events,name="All Events"),
    path('addEvent',views.addEvent,name="Add Event"),
    path('dashboard',views.dashboard,name="Dashboard"),
    path('details/<str:slug>',views.details,name="Event Details"),
    path('login',views.handleLogin,name="Login"),
    path('register',views.handleSignin,name="Register"),    
    path('logout',views.handleLogout,name="Logout"),
    path("edit/<str:slug>",views.editEvent,name="Edit Event"),
    path("delete/<str:slug>",views.deleteEvent,name="Delete Event"),
    path("search",views.search,name="Search Event"),
]
