# from flask_smorest import Blueprint, abort
# from flask import request, jsonify

# def create_user_blueprint(mysql):
#     user_blp = Blueprint('user_routes', __name__, url_prefix='/users')


#     # 전체 유저 데이터를 불러오는 코드
#     @user_blp.route('/', methods=['GET'])
#     def get_users():
#         cursor = mysql.connection.cursor()     # mysqldb를 사용하기 위해서는 cursor 내장함수를 사용할 필요가 있다.
#         cursor.execute("SELECT * FROM users")
        
#         # 튜플형태의 users
#         users = cursor.fetchall()                      # 전체 데이터를 불러오기 때문에 fetchall()쓴다. / return 결과 타입은 tuple로 반환된다.
#         cursor.close()

        
#         users_list = []
#         # REST API로 내려줄 때 dict형태로 받아야 한다.
#         # users의 tuple형태 데이터를 for 반복문을 통해 받아와서 users_list에 dict형태로 담아준다.
#         for user in users:
#             users_list.append({
#                 'id' : user[0],
#                 'name' : user[1],
#                 'email' : user[2]
#             })
#         return jsonify(users_list)
    
#     # 유저를 생성하는 함수
#     @user_blp.route('/', methods=['POST'])
#     def add_user():
#         user_data = request.json
#         cursor = mysql.connection.cursor()
#         cursor.exectue("INSERT INTO users (name, email) VALUES (%s, %s)",
#                        (user_data['name'], user_data['email']))
#         mysql.connection.commit()
#         cursor.close()
    
#         return {'msg':'successfully added user'}, 201
    





# # 새싹반 강사님 솔루션
# from flask_smorest import Blueprint, abort
# from flask import request

# # mysql이 def로 정의되지 않아서 /users에서 데이터베이스에 접근할 수 없음. 500 Internal Server Error 출력
# user_blp = Blueprint('user_routes', __name__, url_prefix='/users')

# @user_blp.route('/', methods=['GET'])
# def get_users():
#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall() # fetchall()의 결과 값은 튜플 데이터
#     cursor.close()

#         # 튜플을 딕셔너리로 변환
#     users_list = []
#     for user in users:
#         users_list.append({
#             'id': user[0],
#             'name': user[1],
#             'email': user[2]
#         })

#     return users_list

# @user_blp.route('/', methods=['POST'])
# def add_user():
#     user_data = request.json
#     cursor = mysql.connection.cursor()
#     cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", 
#                     (user_data['name'], user_data['email']))
#     mysql.connection.commit()
#     cursor.close()
#     return {'message': 'User added successfully'}, 201
