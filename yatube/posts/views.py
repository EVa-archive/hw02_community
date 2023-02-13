from django.shortcuts import render, get_object_or_404
from .models import Group, Post

def index(request):
    posts = Post.objects.select_related('group').order_by('-pub_date')[:10]
    title = 'Главная страница Yatube'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related('group').filter(group=group).order_by('-pub_date')[:10]
    title = group.title
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
 