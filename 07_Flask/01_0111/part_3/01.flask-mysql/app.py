from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
# from user_routes import create_user_blueprint
from user_routes import user_blp    # 새싹반 강사님 대안

app = Flask (__name__)

# Mysql 연동 설정
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1685'
app.config['MYSQL_DB'] = 'OZ'

mysql = MySQL(app)


# blueprint 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# user_blp = create_user_blueprint(mysql)
api = Api(app)
api.register_blueprint(user_blp)




# html 코드로 flask-mysql 테스트
from flask import render_template
@app.route('/users_interface') 
def users_interface():
    return render_template("users.html")