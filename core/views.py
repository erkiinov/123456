from django.shortcuts import render
from .models import *

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'examp.html', context)

def chart2(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'chart2.html', context)

def chart3(request):
    posts = Post3.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'chart3.html', context)

def chart4(request):
    posts = Post4.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'chart4.html', context)

def chart5(request):
    posts = Post5.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'chart5.html', context)

def chart6(request):
    posts = Post6.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'chart6.html', context)