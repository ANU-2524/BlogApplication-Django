from django.urls import path
from . import views
urlpatterns = [
    # path("" , views.check) ,n 
    path("loginn/" , views.loginn , name="loginn") ,
    path("" , views.signup),
    path("home/" , views.home , name="home"),
    path("mypost/" , views.myPost),
    path("newpost/" , views.newPost , name="newpost"), 
    path("signout/" , views.signOut),
    path("like/<int:post_id>/", views.like_post, name="like_post"),
    
]
