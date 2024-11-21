from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }

    return render(request, 'blog_list.html', context)

# 블로그 상세페이지 작성
def blog_detail(request, pk):   # 본래 id값을 받지만 pk로 통일
    blog = get_object_or_404(Blog, pk=pk)   # 없는 pk값을 받을 시 오류가 나기 때문에 변경
    context = {'blog': blog}
    return render(request, 'blog_detail.html', context)