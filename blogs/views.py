from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def post_by_category(request, category_id):
    
    # Fetch the posts that belongs to the category with the  id category_id
    
    posts = Blog.objects.filter(status = 'Published', category = category_id)
    
    # use try except when we do some custom actions if the category does not exist 
    
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect user to home page 
    #     return redirect('home')
    
    
    # use get object or 404 when you want to show page 404 error 
    category = get_object_or_404(Category, pk = category_id)
    
    context = {
        'posts' : posts,
        'category':category,
    }
    
    return render (request, 'post_by_category.html', context)