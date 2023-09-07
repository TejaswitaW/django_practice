from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import Http404
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['id']
    # paginate_by = 3
    paginate_by = 3
    paginate_orphans = 2

   
    def paginate_queryset(self,queryset,page_size):
        try:
            return super(PostListView,self).paginate_queryset(queryset,page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView,self).paginate_queryset(queryset,page_size) 
        

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'