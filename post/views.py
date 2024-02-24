from django.shortcuts import render
from  .models import *
# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    context = {

        'posts': posts
    }
    
    return render(request, 'post/post_index.html', context) 
