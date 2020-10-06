from django.views.generic import ListView, CreateView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class PostCreateView(CreateView):
    model = Post
    template_name = 'create_post.html'

