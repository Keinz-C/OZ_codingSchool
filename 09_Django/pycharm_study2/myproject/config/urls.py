"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render, redirect
from bookmark import views

movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '윙카', 'director': '폴 킹'},
    {'title': '듄: 파트 2', 'director': '드니 빌뇌브'},
    {'title': '시민덕희', 'director': '박영주'},
]

# book_lists = [
#     {'title': '홍학의 자리', 'author': '정해연'},
#     {'title': '군주론', 'author': '니콜론 마키아벨리'},
#     {'title': '언더그라운드', 'author': '무라카미 하루키'},
#     {'title': '나미야 잡화점의 기적', 'author': '히가시노 게이고'},
# ]

def index(request):     # 기본적으로 request를 받음.
    return HttpResponse('<h1>hello</h1>')

def book_list(request):

    # book_text = ''
    #
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'

    return render(request, template_name='booklist.html', context={'range': range(0, 10)})
def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return render(request, template_name='book_detail.html', context={'num':num})

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.')

def python(request):
    return HttpResponse('python 페이지입니다.')

def movies(request):
    # movie_titles = [
    #     f'<a href="/movie/{index}/">{movie['title']}</a><br>' for index, movie in enumerate(movie_list)
    # ]   # list 컴프레이션

    # 아래의 for문과 위의 for문은 같은 내용이다.
    # movie_titles = []
    # for movie in movie_list:
    #     movie_titles.append(movie['title'])

    # response_text = '<br>'.join(movie_titles)

    # movie 화면단에서 목록을 클릭하면 해당 화면으로 넘어가도록 href 설정
    # enumerate는 index와 title에 for문을 돌면서 나오는 객체를 전달한다.
    # for index, title in enumerate(movie_titles):
    #     response_text += f'<a href="/movie/{index}/">{title}</a><br>'

    # return HttpResponse(response_text)
    return render(request, template_name= 'movies.html', context={'movie_list': movie_list})


def movie_detail(request, index):
    # movie_list는 0, 1, 2, 3의 4개의 dict값을 가지고 있다.
    if index > len(movie_list) -1:  # len으로 할 경우 숫자가 4가 나오기 때문에 -1로 범위를 맞춰준다.
        raise Http404

    movie = movie_list[index]
    # context = {'movie_list': movie_list, 'index': index}
    context = {'movie': movie}
    return render(request, template_name='movie.html', context=context)

def gugudan(request, dan):
    if dan < 2:
        # from django.shortcuts에 있는 기능
        return redirect('/gugu/2/')


    # context = {
    #     'dan': dan,
    #     'results': [dan * i for i in range(1, 10)]
    # }
    # context = {
    #     'dan': dan,
    #     'results': [(i, dan * i) for i in range(1, 10)]
    # }
    context = {
        'dan': dan,
        'range': range(1, 10)
    }

    return render(request, template_name="gugudancal.html", context=context)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    # path('book_list/', book_list),
    # path('book_list/<int:num>/', book),  # book_list로 값이 들어와 num의 값을 book의 num 매개변수에 값을 전달하여 실행한다.
    # path('language/python/', python),   # 해당 path를 str path 위에 놓으면 먼저 화면단에 보여줄 수 있다.
    # path('language/<str:lang>/', language), # 특별한 경우가 아니라면 str은 자주 사용하지 않는다.
    # path('movie/', movies),
    # path('movie/<int:index>/', movie_detail),
    # path('gugu/<int:dan>/', gugudan),
    path('bookmark/', views.bookmark_list),
    path('bookmark/<int:pk>/', views.bookmark_detail),

]
