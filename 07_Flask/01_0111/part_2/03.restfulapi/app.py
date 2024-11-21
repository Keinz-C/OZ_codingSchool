from flask import Flask
from flask_restful import Api
from resources.item import Item

app = Flask(__name__)
# app이라는 flask 개체를 만들고, 이 app 개체가 다른 라이블리에서 필요하여 이것을 넘겨주는 과정을 이니셜라이징이라고 한다.
api = Api(app)



# 리소스를 할당하고 아래 코드를 작성해야 리소스가 등록이 된다.
api.add_resource(Item, '/item/<string:name>')    # 경로 추가