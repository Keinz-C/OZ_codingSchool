import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

SearchWord = input('검색할 키워드를 작성해주세요.')     # 1. 키워드를 입력 받아
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + SearchWord   # 2. 입력받은 값을 url에 더해 변수에 담

req =requests.get(url, headers=header_user)      # 3. url의 html 정보를 요청해서 받아오고

html = req.text     # 4. 받은 html정보를 req에 담아 text만 추출하여 html변수에 담고
soup = BeautifulSoup(html, 'html.parser')       # 5. BeautifulSoup을 통해 html의 내용에서 원하는 내용을 parser 구조로 찾아낸다.

# 위의 코드는 정적 웹페이지 크롤링의 가장 기본적인 형태로, url만 변경하여 사용하면 된다.

name = soup.select('.name')      # 여기서 select는 ctrl+f처럼 찾는 키워드를 전부 찾는다. / css에서 클래스는 . id는 #
# <a href="https://blog.naver.com/lune_etoile/223578861943" class="title_link" data-cb-trigger="" data-cb-target="90000003_00000000000000340E56B177" onclick="return goOtherCR(this,'a=blg*a.nblg&amp;r=1&amp;i=90000003_00000000000000340E56B177&amp;u='+urlencode(this.href));" target="_blank">2024년 09월 10일 오만 대한민국 중계 오만전 한국 축구 하이라이트 골장면 <mark>손흥민</mark> 북중미 월드컵 3차 예선</a>

# css에서 a태그 밑의 일부를 선택하는 방법을 채택
name = soup.select('.user_info > a')

title = soup.select('.title_link')
# soup.select_one -> 원하는 정보 1개만 찾을 수 있음
# 클래스 명이 2개일 때(spblog ico_ad) -> (".spblog.icd_ad")

# 광고 제외 검색
pass_ad = soup.select('.spblog','.ico_ad')
# 검색어는 꿀

for i in zip(title, name, pass_ad):      # title [0], name [1]
    print(f'블로그 제목 : {i[0].text}')
    print(f'작성자 : {i[1].text}')
    if i[1].name == 'a' and 'href' in i[1].attrs:
        print(f'작성자 링크 : {i[1]['href']}')
    else:
        print("작성자 링크 없음")
    print()