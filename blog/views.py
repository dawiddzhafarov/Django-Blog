from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Lolek',
        'title': 'Blog Post 1',
        'content': 'First content',
        'date_posted': "August 27, 2018"
    },
{
        'author': 'Bolek',
        'title': 'Blog Post 2',
        'content': 'Second content',
        'date_posted': "August 28, 2018"
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context,)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})