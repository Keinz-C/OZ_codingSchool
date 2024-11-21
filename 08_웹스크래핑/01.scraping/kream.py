from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options   # 강제로 연 브라우저에 몇 가지 옵션을 넣을 수 있는 블럭
import time

from selenium.webdriver.common.by import By     # css 문법을 이해시키기 위한 모듈
from selenium.webdriver.common.keys import Keys # 키 입력을 이해시키기 위한 모듈

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

options = Options()
# 유저 정보를 전달하여 실제 사용자가 이용하는 것처럼 만들기
options.add_argument(f'User-Agent={user}')
# 페이지 크기가 안 맞을시 처 시작 윈도우 화면을 조정하는 코드
# options.add_argument("--window-size=1200,4500")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ['enable=logging'])

driver = webdriver.Chrome(options=options)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("supreme")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

# 웹 페이지 검사를 통한 코드를 가져오는 것과 같음.
html = driver.page_source
# 웹 페이지를 문자로만 읽기 때문에 트리 구조를 통해 크롤링 가능하도록 BeautifulSoup을 사용
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

for item in items:
    product_name = item.select_one('.translated_name').text
    if "후드" in product_name:
        product_brand = item.select_one(".product_info_brand.brand").text
        product_price = item.select_one(".amount").text

        print(f'상품명 : {product_name}')
        print(f'브랜드 : {product_brand}')
        print(f'가격 : {product_price}')
        print()

driver.quit()