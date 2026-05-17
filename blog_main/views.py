
from django.shortcuts import render , redirect
from blogs.models import Category, Blog
from about_links.models import About, Links



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