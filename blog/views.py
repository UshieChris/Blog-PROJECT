from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'come.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'creat.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model =Post
    template_name = 'edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy("home")








