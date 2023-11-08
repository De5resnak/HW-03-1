from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from datetime import datetime

# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = '-article_date'
    template_name = 'posts.html'
    context_object_name = 'posts'

class PostDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'