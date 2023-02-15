from django.shortcuts import render, get_object_or_404
from .models import Group, Post
COUNTER_POSTS = 10


def index(request):
    posts = Post.objects.all()[:COUNTER_POSTS]
    context = {
        'title': 'Главная страница Yatube',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group.all()[:COUNTER_POSTS]
    context = {
        'title': group.title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
