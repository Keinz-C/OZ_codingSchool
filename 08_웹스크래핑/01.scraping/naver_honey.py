import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

SearchWord = input('검색할 키워드를 작성해주세요.') 
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + SearchWord

req =requests.get(url, headers=header_user)  

html = req.text
soup = BeautifulSoup(html, 'html.parser') 

# 블로그의 제목, 작성자, 하이퍼링크를 css구성에 맞춰 class를 찾아 가져옴(해당 view_wrap인 div안에 제목, 작성자, 링크등이 속해있음)
view = soup.select('view_wrap')



for i in view:
    title = i.select_one('.title_link')
    name = i.select_one('.user_info > a')
    ad = i.select_one('.spblog.ico_ad')

    # if not의 경우 ad에 값이 들어가면 pass, 값이 들어가지 않다면 아래 프린트문을 출력한다.
    if not ad:
        print(f'블로그 제목 : {title.text}')
        print(f'작성자 : {name.text}')
        print(f'블로그 링크 : {name['href']}')
        print()