from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Category, Tag


def index(request):
    # return HttpResponse('Hello World!')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html',context={'post_list':post_list,'title':'jacklee blog','welcome':'welcome to my blog'})

def test(request):
    post_list = Post.objects.all()
    return render(request,'blog/test.html', context={'post_list':post_list})