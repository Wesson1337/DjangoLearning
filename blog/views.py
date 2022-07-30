from django.shortcuts import render
import logging
from blog.models import Post

logger = logging.getLogger(__name__)


def post_view(request):
    posts = Post.objects.select_related('blog').prefetch_related('author').all()
    logger.info('Запрошена страница со списком записи')
    return render(request, 'blog/posts.html', context={'posts': posts})
