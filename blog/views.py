from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.contrib import messages
from django.db.models import Q


def index(request):
    blog = Blog.objects.order_by('-id')
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')
    if keyword:
        """ テキスト用のQオブジェクトを追加 """
        blog = blog.filter(
            Q(title__icontains=keyword) | Q(text__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, 'blog/index.html', {'blog': blog})


def detail(request, blog_id):
    blog_text = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/detail.html', {'blog_text': blog_text})
