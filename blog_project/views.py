from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request,category_slug=None):
    post = Post.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug = category_slug)
        post=Post.objects.filter(category=category)
   
       
    category=Category.objects.all()

    return render(request,'index.html',{'post':post,'category':category})