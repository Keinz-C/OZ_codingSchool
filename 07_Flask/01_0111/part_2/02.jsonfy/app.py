from flask import Flask, jsonify, request

app = Flask(__name__)

# GET
# (1) 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}  # dict형태이기 때문에 return을 jsonify로 감싸지 않아도 된다.

    return data


# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result':'success', 'data':{'feed1':'data1'}}

    return data


# POST
# (1) 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']

    print(name, age)
    return jsonify({'result':'success'})

datas = [{"items": [{"name": "item1", "price": 10}]}]   # dict형태의 데이터를 json에서 할당하기 위해서는 ""을 사용해야한다.

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {"datas":datas}

@app.route('/api/v1/datas', methods=['POST'])
def creata_data():
    request_data = request.get_json()    # 들어오는 데이터를 json형태로 받겠다는 내장함수

    new_data = {'items': request_data.get("items", [])}
    datas.append(new_data)

    return new_data, 201            # 201은 status코드이다.