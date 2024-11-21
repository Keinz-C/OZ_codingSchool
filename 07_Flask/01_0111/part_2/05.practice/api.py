from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema      # schemas 파일에서 BookSchema 클래스 구성을 참조한다.

# 각 api를 묶어서 구성시키기 위해 book_blp라는 변수에 할당
# url과 아래 함수 매핑을 관리하기 위해 Blueprint를 사용한다. 
# 첫 번째 books는 Blueprint의 별칭, 두번째 books는 Blueprint에 들어갈 값을 지정한다.
# descripiton은 이후 swaggerui를 사용할 때 어떤 api인지 설명하는 기능
book_blp = Blueprint("books", "books", url_prefix="/books", description="Operations on books")

# 간단한 DB 대체
books = []

# 새로운 books데이터를 추가하는 Post하고, 조회하는 get 작성
@book_blp.route('/')
class BookList(MethodView):     # BookList는 여러개의 데이터를 가져올 때 사용한다
    @book_blp.response(200, BookSchema(many=True))      # many는 list데이터에 한하는 함수로, 저장되어 있는 전체 데이터를 보여줄 때 사ㅛㅇ한다.
    def get(self):
        return books
    

    @book_blp.arguments(BookSchema)     # 새로운 값을 post할 때, BookSchema 구조에 부합한지 확인하는 내장함수
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        # len을 통해 books의 기존 데이터값에 1씩 증가시켜 id값에 할당되도록 설정한 하드코딩
        new_data['id'] = len(books) + 1
        books.append(new_data)
        return new_data

# DB상의 데이터를 조회하는 get
@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)    # books 리스트를 book안에 반복적으로 할당하고, 이 값들 중 book_id 를 조회할 때 같은 book_id가 있다면 조회, 아니라면 abort로 에러페이지 전송
        if book is None:
            abort(404, message="Book not found")
        return book

    # put의 경우 update이기 때문에 우선 BookSchema구조에 부합한지 검증한다.
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        book.update(new_data)
        return book

    @book_blp.response(204)
    def delete(self, book_id):
        global books
        if not any(book for book in books if book["id"] == book_id):
            abort(404, message="Book not found")
        books = [book for book in books if book["id"] != book_id]
        return ''