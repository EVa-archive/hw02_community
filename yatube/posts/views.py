from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Group, Post
COUNTER_POSTS = 10


def index(request):
    # posts = Post.objects.all()[:COUNTER_POSTS]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, COUNTER_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Главная страница Yatube',
        # 'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # posts = group.group.all()[:COUNTER_POSTS]
    post_list = group.group.all()
    paginator = Paginator(post_list, COUNTER_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': group.title,
        'group': group,
        # 'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)
