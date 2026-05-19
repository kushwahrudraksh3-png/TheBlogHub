
from django.shortcuts import render , redirect
from blogs.models import Category, Blog
from about_links.models import About, Links
from . forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def home(request):
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True, status = 'Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured = False, status = 'Published')

    # Fetch about us data 
    try:
        about = About.objects.get()
    except:
        about = None
    
    
    
    context = {
        # 'categories': categories,
        'featured_posts' : featured_posts,
        'posts':posts,
        'about': about,
    }
    return render(request , 'home.html', context)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    
    context = {
        'form':form,
    }
    return render(request, 'register.html' ,context)





def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    
    print(request.user.username)
    return render(request, 'login.html', context)



def logout(request):
    auth_logout(request)
    return redirect('home')