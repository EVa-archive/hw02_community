from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Group, Post
from django.contrib.auth.models import User
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
    teamplate = 'posts/group_list.html'
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
    return render(request, teamplate, context)


def profile(request, username):
    teamplate = 'posts/profile.html'
    user_profile = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author__username=username).all()
    post_count = post_list.count()
    paginator = Paginator(post_list, COUNTER_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user_profile': user_profile,
        'username': username,
        'title': f'Профайл пользователя {username}',
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, teamplate, context)


def post_detail(request, post_id):
    teamplate = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    post_count = Post.objects.filter(author=post.author).count()
    post_text = post.text[:30]
    context = {
        'title': f'Пост {post_text}',
        'post': post,
        'post_count': post_count,
    }
    return render(request, teamplate, context)
