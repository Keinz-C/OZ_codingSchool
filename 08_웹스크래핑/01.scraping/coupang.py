import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36","accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

keyword = input("검색어를 입력해주세요.")
url = f"https://www.coupang.com/np/search?component=178155&q={keyword}"
cookie = {"cho","student"}

req =requests.get(url, timeout=3, headers=header_user)  


html = req.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.select(".search-product  ")

# for item in items:
#     num = item.select_one('.number')
#     rocket = item.select_one('.badge.rocket')
#     if num and rocket == True:
#         name = item.select_one(".name").text
#         price = item.select_one(".price-value").text
#         link = item.a["href"]

#         print(f'순위 : {num.text}')
#         print(f'제품명 : {name}')
#         print(f'금액 : {price}')
#         print(f'링크 : https://www.coupang.com/{link}')
#         print(f'로켓배송 가능')
#         print()
#     else:
#         print("로켓 배송 불가 상품")
#         print()

for item in items:
    num = item.select_one('.number')
    if num:
        name = item.select_one(".name").text
        price = item.select_one(".price-value").text
        link = item.a["href"]
        rocket = item.select_one('.badge.rocket')

        print(f'순위 : {num.text}')
        print(f'제품명 : {name}')
        print(f'금액 : {price}')
        print(f'링크 : https://www.coupang.com/{link}')
        if rocket:
            print('로켓배송 가능')
        else:
            print('로켓배송 불가')