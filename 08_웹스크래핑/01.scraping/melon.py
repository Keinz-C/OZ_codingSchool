import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"

req =requests.get(url, headers=header_user)  

html = req.text
soup = BeautifulSoup(html, 'html.parser')

lst50 = soup.select('.lst50')
lst100 = soup.select('.lst100')

lst_all = lst50 + lst100
# soup.find_all(class_=["lst50", "lst100"])

# enumerate(반복할 변수 & 객체 & 데이터, 1) 뒤에 시작할 숫자만 넣어주면 됨. -> 앞의 변수,객체,데이터와 뒤의 숫자가 매칭됨.
for rank, i in enumerate(lst_all, 1):
    # > a를 쓰지 않는 이유는 > 해당 기호느 바로 다음을 칭한다. a태그를 선택한다면 기호를 빼고 작성한다.
    title = i.select_one(".ellipsis.rank01 a").text
    artist = i.select_one(".ellipsis.rank02 a").text
    album = i.select_one(".ellipsis.rank03 a").text
    print(f'[순위] : {rank}')
    print(f'[제목] : {title}')
    print(f'[가수] : {artist}')
    print(f'[앨범] : {album}')
    print()