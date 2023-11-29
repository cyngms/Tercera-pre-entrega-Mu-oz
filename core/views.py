from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Author, Post, Comment
from .forms import AuthorForm, PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'blog/author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'blog/author_detail.html'


class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'])


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'blog/author_form.html'
    success_url = '/'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.kwargs['pk']})


class SearchView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        else:
            return Post.objects.all()
