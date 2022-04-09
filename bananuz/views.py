from django.shortcuts import render
from .models import *


def base(request):
    category = Category.objects.all()
    province = Province.objects.all()
    return render(request , 'base.html', {'categories':category , 'provinces':province})

def home(request):
    category = Category.objects.all()
    province = Province.objects.all()
    post = Post.objects.all()
    return render(request , 'home.html', {'categories':category , 'provinces':province, 'posts':post})

def category(request, slug):
    category_all = Category.objects.all()
    category = category.objects.get(slug__iexact=slug)
    posts = category.post_set.order_by('-date')
    province = Province.objects.all()
    return render(request , 'category.html', {
        'categories':category_all ,
        'category':category,
        'posts':posts,
        'provinces':province,
        })

def province(request, slug):
    category_all = Category.objects.all()
    province_all = Category.objects.all()
    province = Province.objects.get(slug__iexact=slug)
    posts = province.post_set.order_by('-date')
    return render(request , 'category.html', {
        'categories':category_all ,
        'province':province_all,
        'provinces':province,
        'posts':posts,
        })

