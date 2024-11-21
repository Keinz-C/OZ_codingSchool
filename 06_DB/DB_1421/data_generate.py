import mysql.connector
from faker import Faker
import random   # random은 파이썬 기본 모듈

# 1. mysql 연결 설정
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1685',
    database = 'chapter17'
)

# 2. mysql 연결
cursor = db_connection.cursor()
faker = Faker()     # faker는 데이터를 랜덤으로 generate하기 위해 사용하는 모듈

# users 데이터 생성
# users 데이터가 먼저 있어야, orders 데이터에서 폴인키로 연결해서 데이터를 만들 수 있기 때문이다.
for _ in range(100):    # _는 값을 사용하지 않고 100번을 반복하기 위해서 작성했다.
    username = faker.user_name()    # 더미 데이터
    email = faker.email()           # 더미 데이터

    sql = "INSERT INTO users(username, email) VALUES(%s, %s)"   # %s는 str데이터를 입력하겠다는 것
    values = (username, email)   

    cursor.execute(sql, values)             # 쿼리를 실행해달라는 명령문. 각각의 반복문이 돌면서 하나씩 생성된 값들이 sql과 values의 db로 전달이 된다.

# user_id 불러오기
# 이때 더미 데이터를 만들기 위해서 user_id값을 넣어야 되는데, 존재하지 않는 user_id값을 orders에 넣게 되면 문제가 생긴다.
cursor.execute("SELECT user_id FROM users")

# cursor에 데이터가 담겨 있어 데이터를 전부 가져온다.
# list로 만들어 cursor에 담긴 데이터는 fetchall()로 전부 가져와 row에 데이터가 들어오고, row데이터에서 0번째 데이터를 가져와서 user_id로 쓰겠다는 것이다.
# 데이터는 개체형태이기 때문에 원하는 첫 번째 데이터는 user_id기 때문에 그것을 반복하겠다는 것이다.
valid_user_id = [row[0] for row in cursor.fetchall()] 


# 100개의 주문 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)      # user_id는 valid_user_id에 담긴 데이터 중에서 랜덤하게 선택하겠다
    product_name = faker.word()                 # 단어를 랜덤하게 만들어내는 함수
    quantity = random.randint(1, 10)            # quantity를 1 ~ 10까지 숫자중 랜덤하게 하나를 수량으로 넣겠다
    
    try:                          # DB에 잘 들어갔는지 확인하기 위해 try문을 작성하여 확인한다.
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)  # 보통 변수를 만들때는 컬럼명이랑 동일하게 만드는 것이 덜 헷갈린다.
    
        cursor.execute(sql, values)
    except mysql.connector.Error as err:
        print(f'오류발생: {err}')
        pass





db_connection.commit()
cursor.close()
db_connection.close()