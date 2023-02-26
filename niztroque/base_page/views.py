from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def register(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'base_page/base_page.html',context)