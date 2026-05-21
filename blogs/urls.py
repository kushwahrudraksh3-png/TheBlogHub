from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.post_by_category, name='post_by_category'),
    path('like/<slug:slug>/', views.like_blog, name='like_blog'),
    path('save/<slug:slug>/', views.save_blog, name='save_blog'),
    
    
]
