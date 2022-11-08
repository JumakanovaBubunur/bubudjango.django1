from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.
def hello(request):
    return HttpResponse('<h1> Hello world</h1>')

def blog_all(request):
    post = models.Post.objects.all ()
    return render(request, 'post_list.html', {'post': post})
