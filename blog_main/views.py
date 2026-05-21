
from django.shortcuts import render , redirect
from blogs.models import *
from about_links.models import About, Links
from . forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



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
            return redirect('login')
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
            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('home')
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



def profile(request):
    liked_blogs = BlogLike.objects.filter(user= request.user)
    saved_blogs = BlogSave.objects.filter(user= request.user)
    comment_blogs = Comment.objects.filter(user= request.user)
    
    print(comment_blogs)
    
    like_count = liked_blogs.count()
    save_count = saved_blogs.count()
    comment_count = comment_blogs.count()
    
    context = {
        'liked_blogs':liked_blogs,
        'saved_blogs':saved_blogs,
        'comment_blogs':comment_blogs,
        'like_count':like_count,
        'save_count':save_count,
        'comment_count':comment_count,
        
    }
    return render(request, 'profile.html', context )


@login_required(login_url='login')
def edit_profile(request):

    if request.method == "POST":
        user = request.user

        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        if user.is_staff:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')

        user.save()

        return redirect('profile')

    return render(request, 'edit_profile.html')
   

@login_required(login_url='login')
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            user=request.user,
            data=request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)

            return redirect('profile')

    else:

        form = PasswordChangeForm(user=request.user)

    context = {
        'form': form
    }

    return render(
        request,
        'change_password.html',
        context
    )