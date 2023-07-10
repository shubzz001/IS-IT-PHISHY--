
from django.contrib import admin
from django.urls import path
from firstapp import views



urlpatterns = [
   path("home",views.index,name="home"),
   path("about",views.about,name="about"),
   path("contact",views.contact,name="contact"),
   path("complaint",views.complaint_post,name="complaint"),
   path("login",views.login_post,name="login"),
   path("",views.signup_post,name="signup"),
   path("logout",views.logout_post,name="logout"),
   
]
   

