from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board

app = Flask(__name__)

# app.config를 통한 데이터베이스와 연결시키는 코드
# 뒤의 코드는 설치된 mysql 데이터베이스에 연동 및 접속을 위한 코드 / mysql(접속할 db)+pymysql(연결을 위한 코드)://root(db name):password(db PW)@localhost(db 접속경로)/ozz(접속할 db명)
# config는 기본설정을 사용하는 코드
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1685@localhost/ozz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        # 객체가 바뀔 때마다 TRACKING 여부에 대해 메모리 과부화를 피하기 위해서 기본적으로 False
db.init_app(app)

# blueprint 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

# app.py에 blueprint 등록
from routes.board import board_blp
from routes.user import user_blp
api.register_blueprint(board_blp)
api.register_blueprint(user_blp)

from flask import render_template
@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__ == '__main__':
    with app.app_context():
        print("bugs here")
        db.create_all()         # 이미 db가 생성되어 있고, 원하는 대로 모델이 반영되면 그대로 / 아니면 pass
    app.run(debug=True)