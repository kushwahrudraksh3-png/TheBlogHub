from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
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



def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status= 'Published')
    
    liked = False
    saved = False

    if request.user.is_authenticated:
        liked = BlogLike.objects.filter(user=request.user, blog=single_blog).exists()
        saved = BlogSave.objects.filter(user=request.user, blog=single_blog).exists()

    like_count = BlogLike.objects.filter(blog=single_blog).count()  
    save_count = BlogSave.objects.filter(blog=single_blog).count()
    
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        
        comment.save()
        return HttpResponseRedirect(request.path_info)
        
    
    # comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    
    context = {
        'single_blog': single_blog,
        'comments':comments,
        'comment_count' : comment_count,
        'liked': liked,
        'saved': saved,
        'like_count': like_count,
        'save_count': save_count,
    }
    
    return render(request, 'blogs.html' , context )



def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status = 'Published')
    
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    
    return render(request, 'search.html', context)



@login_required(login_url='login')
def like_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    like = BlogLike.objects.filter(user=request.user, blog=blog)

    if like.exists():
        like.delete()
    else:
        BlogLike.objects.create(user=request.user, blog=blog)

    return redirect('blogs', slug=slug)


@login_required(login_url='login')
def save_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    save = BlogSave.objects.filter(user=request.user, blog=blog)

    if save.exists():
        save.delete()
    else:
        BlogSave.objects.create(user=request.user, blog=blog)

    return redirect('blogs', slug=slug)