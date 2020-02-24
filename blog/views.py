from django.shortcuts import render

posts = [
    {
        'author': 'Teddy Brown',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted': 'February 18, 2020'
    },
    {
        'author': 'Bob Miller',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'February 18, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})