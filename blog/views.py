from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.contrib import messages
from django.db.models import Q

from django.views import generic


class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'
    """ オーバーライド """

    def get_queryset(self):
        queryset = Blog.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset


class DetailView(generic.DeleteView):
    template_name = 'blog/detail.html'
    model = Blog
