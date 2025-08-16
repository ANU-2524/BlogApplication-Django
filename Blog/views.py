from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from . import models 


def check(request):
    return render(request, 'blog/base.html')

def loginn(request) :
    if (request.method == 'POST') :
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request , username = name , password = password )
        if userr is not None :
            login(request , userr)
            return redirect('home')
        else :
            return redirect('loginn') 
    return render(request , 'blog/login.html') 

def signup(request) :  
    if request.method == 'POST' :
        name  = request.POST.get('uname')
        email  = request.POST.get('uemail')
        password  = request.POST.get('upassword')
        newUser = User.objects.create_user(username = name, email = email , password = password) 
        newUser.save()
        return redirect('loginn')       
    return render(request ,'blog/signup.html')

def home(request) :
    context = {
        'posts' : Posts.objects.all()
    }
    return render(request , 'blog/home.html' , context )

@login_required(login_url="loginn")
def newPost(request) :
    if request.method == "POST" :
        title = request.POST.get("title")
        content = request.POST.get("content")
        npost = models.Posts.objects.create(title = title , content = content , author = request.user)
        npost.save()
        return redirect("home")
    return render(request , 'blog/newpost.html')

@login_required(login_url = "loginn")
def myPost(request) :
    # print(author)
    print("req", request.user)
    context = {'posts' : Posts.objects.filter(author_id = request.user.id )}
    return render(request , 'blog/mypost.html' , context)

def signOut(request) :
    logout(request )
    return redirect("loginn")
    
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)   # unlike
    else:
        post.likes.add(request.user)     # like
    return redirect('/home')   # or use reverse('home')