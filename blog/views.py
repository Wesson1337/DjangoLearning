from django.shortcuts import render

from blog.models import Post


def post_view(request):
    posts = Post.objects.select_related('blog').prefetch_related('author').all()
    return render(request, 'blog/posts.html', context={'posts': posts})
