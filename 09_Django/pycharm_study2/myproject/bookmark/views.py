from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from bookmark.models import Bookmark

# 메인 알고리즘을 담당하는 파이썬
# new *

def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(id__gte=50)
    # objects.all = SELECT * FROM bookmark_bookmark / mysql의 쿼리문과 같다.

    context = {
        'bookmarks': bookmarks
    }
    return render(request, template_name='bookmark_list.html', context=context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    #     [Bookmark: Bookmark = Bookmark.objects.get(pk=pk) = SELECT * FROM bookmark WHERE id=id LIMIT 1]
    #     [Bookmark: [Bookmark(목록)] = Bookmark.objects.filter(pk=pk, name='네이버') = SELECT * FROM bookmark WHERE id=id or name='네이버'] / 전부 불러옴
    #     [Bookmark: [Bookmark(목록)] = Bookmark.objects.filter(name__icontains='네이') = SELECT * FROM bookmark WHERE LIKE '%네이버%']

    #     now = datetime.now()                                             gt=now / lte=now / lt=now / id__gte=2
    #     [Bookmark: [Bookmark(목록)] = Bookmark.objects.filter(created_at__gte=now) = SELECT * FROM bookmark WHERE created_at >= now]

    # except:
    #     raise Http404

    # django의 내장 함수, 위의 try except 문을 간단하게 바꾼 내용
    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {
        'bookmark': bookmark
    }
    return render(request, template_name='bookmark_detail.html', context=context)