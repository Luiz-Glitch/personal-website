from django.shortcuts import render

from .models import Post

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context)

def about_view(request):
    return render(request, 'about.html')
