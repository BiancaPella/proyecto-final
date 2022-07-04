from ast import Del
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from setuptools import Command
from .models import Comment, Post
from .forms import ComentarioForm, PostForm, EditForm

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

class PostsView (ListView):
    model = Post
    template_name = 'posts.html'
    ordering = ['-post_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PublicarView(CreateView):
    model = Post
    form_class=PostForm
    template_name = "publicar.html"
    #fields = '__all__'

class EditarPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editar_post.html'
    #fields = ['title', 'title_tag', 'body']

class EliminarPostView(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('posts')

class ComentarView(CreateView):
    model = Comment
    form_class=ComentarioForm
    template_name = "agregar_comentario.html"
    ordering = ['-date_added']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('posts')

def resultado(request):
    if request.method == "POST":
        busqueda = request.POST['busqueda']
        post = Post.objects.filter(title__contains=busqueda)
        return render(request, 'resultado_busqueda.html', {'busqueda':busqueda, 'post':post})
    else:
        return render(request, 'resultado_busqueda.html', {})
