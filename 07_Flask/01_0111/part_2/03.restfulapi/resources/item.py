from flask import request
from flask_restful import Api, Resource


items = []  # DB의 대체 역할 (간단한 DB 역할)

class Item(Resource):
    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg":"Item not found"}, 404    # msg는 메시지이고 404는 스테이터스 코드이다.

    # 특정 아이템 생성
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {"msg": "Item Already exists"}, 400
        
        data = request.get_json()

        new_item = {'name':name, 'price': data['price']}
        items.append(new_item)

        return new_item     # 포스트를 사용할 때에는 새로 생성하는 데이터 값을 내려주는 것이 일반적이다.

    # 특정 아이템 업데이트
    def put(self, name):
        data = request.get_json()

        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item
            
        # 만약, 업데이트하고자 하는 아이템 데이터가 없다면 -> 추가하는 예시문
        new_item = {'name':name, 'price': data['price']}
        items.append(new_item)

        return new_item

    # 특정 아이템 삭제
    def delete(self, name):
        global items
        
        items = [item for item in items if item['name'] != name]

        return {"msg":"Item Deleted"}
    
    # 코드 해석 : 전역변수 items를 불러오고, item 안에 items의 값만큼 할당을 반복하고 item을 불러서, 만약 item 안에 name이 없다면 해당 아이템을 반환해줘라