from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hellow, This is Main Page!'

# Alt + Shift + 화살표 위, 아래
@app.route('/about')
def about():
    return 'Hellow, This is about Page!'

@app.route('/house')
def house():
    return 'Im home!'

# 파라미터를 숫자형을 받고 싶다면 타입 지정을 해줘야한다.
@app.route('/number/<int:number>')
def number(number):
    return f'number : {number}'

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
@app.route('/user/<username>')
def user_profile(username):

    return f'UserName : {username}'

# post 요청 날리는 법
# (1) postman
# (2) requests
import requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print('GET method')

    if request.method == 'POST':
        print('***POST method***', request.data)

    return Response('Sucessfully submitted', status=200)

if __name__ == '__main__':
    app.run()