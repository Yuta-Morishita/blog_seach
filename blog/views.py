
from .models import Blog

from django.contrib import messages
from django.db.models import Q
from django.views import generic  # クラスリストビュー用
""" 追加 """
from functools import reduce
from operator import and_


class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = Blog.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''
            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i
            query = reduce(
                and_, [Q(title__icontains=q) | Q(text__icontains=q) for q in q_list]
            )
            queryset = queryset.filter(query)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset


class DetailView(generic.DeleteView):
    template_name = 'blog/detail.html'
    model = Blog
    context_object_name = 'blog'
