from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# OpenAPI 관련 설정 / RESTAPI를 예쁘게 보여주는 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)     # blueprint는 api를 만들 때 기능별로 묶어주기 위해 사용하는 함수이다. / api가 복잡해질수록 관리에 용이해진다.

if __name__ == "__main__":
    app.run(debug=True)