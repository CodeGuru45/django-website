from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import code

def home(request):
    context = {
        'posts': Post.objects.order_by('-ratings__average'),
    }
    return render(request, 'blog/home.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.music_link = post.music_link[:24] + '/embed' + post.music_link[24:]
            post.save()
            return redirect('blog-home')
    else:
        form = CreatePostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()

    context = {
        'user_posts': Post.objects.filter(author=request.user),
    }
    return render(request, 'blog/user_posts.html', context)
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user_posts': Post.objects.filter(author=user),
    }
    return render(request, 'blog/user_posts.html', context)