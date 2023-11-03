from django.shortcuts import render

from post.models import Post, ProfileUser

# Create your views here.


def index(request):
  posts = Post.objects.all()
  context= {
      'posts':posts
    }
  return render (request, "index.html", context)


def index2(request):
  return render (request, "instuctors.html")


def index3(request):
  return render (request, "contact.html")




