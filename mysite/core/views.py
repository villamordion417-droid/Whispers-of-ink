from django.shortcuts import render
from writings.models import Post


def home(request):
    # Get the most recent posts
    recent_posts = Post.objects.all()[:6]
    total_posts = Post.objects.count()
    
    context = {
        'recent_posts': recent_posts,
        'total_posts': total_posts,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')
