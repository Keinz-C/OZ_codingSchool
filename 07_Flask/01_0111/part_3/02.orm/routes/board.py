from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# API List
# /board/
# 전체 게시글을 가져오는 API(GET)
# 게시글 작성(POST)
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        # boards 게시글 안에 있는 모든 데이터를 가져오는 .all()
        boards = Board.query.all()

        # 각 게시글의 정보를 가져오는 for문
        # for board in boards:
        #     print('id', board.id)
        #     print('title', board.title)
        #     print('content', board.content)
        #     print('user_id', board.user_id)
        #     print('authord', board.author)  # User를 참조하고 있음
        #     print('authord_name', board.author.name)  
        #     print('authord_email', board.author.email)


        # 위의 프린트 for 반복문을 요약한 jsonify문
        return jsonify([{"id":board.id, 
                         'title':board.title, 
                         'content':board.content, 
                         'author_name':board.author.name}for board in boards
                         ])

    def post(slef):
        # user에게 데이터 받기
        data = request.json
        # 게시글 작성을 위해 모델을 불러온다.
        new_board = Board(
            title=data['title'], 
            content=data['content'], 
            user_id=data['user_id'])
        
        print(new_board)
        # new_board에 만들어진 새 객체를 db에 추가하기 위해 add / 전송을 위해 commit을 사용
        db.session.add(new_board)
        db.session.commit()

        return jsonify({'msg': 'success create board'}), 201


# /board/<int: board_id>
# 하나의 게시글 불러오기(GET)
# 특정 게시글 수정하기(PUT)
# 특정 게시글 삭제하기(DELETE)

# 여러개의 데이터를 다룰때는 list, 하나의 데이터를 다룰때는 classa가 유용함 -> 단, 모델과 이름이 겹치지 않도록 주의
@board_blp.route("/<int:board_id>")
class BoardResource(MethodView):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)

        return jsonify({
            'id':board.id,
            'title':board.title,
            'content':board.content,
            'author':board.author.name
            })

    def put(self, board_id):
        board = Board.query.get_or_404(board_id)

        data = request.json

        board.title = data['title']
        board.content = data['content']
        db.session.commit()

        return jsonify({'msg':'Successfully updated board data'}), 202

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)

        db.session.delete(board)
        db.session.commit()

        return jsonify({'msg':'deleted'}), 204