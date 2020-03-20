from django.shortcuts import render
from .models import Comment
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.filter(ratings__isnull=False).order_by('-ratings__average')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})