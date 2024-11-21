# Model을 만드는 것은 Table을 만드는 것과 동일
# 게시글 model -> board
# 유저 model -> user
# Model은 기본 단수이고, 여러개의 Model을 만들 때에는 s를 붙여 복수로 만든다

from db import db

class User(db.Model):       # 코드 해석 : User Model을 만들 때 db.Model을 상속받도록 하고 싶다.
    __tablename__ = "users"     # user가 여럿 모여있는 정보들이 users라는 table에 담기기 때문에 네이밍을 복수로 지정

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # orm에서 역참조 / board라는 객체에서 back_populates(역참조)로 author를 역참조하고 그 중 (lazy='dynamic')필요한 부분의 쿼리셋을 실행시키겠다.
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')


class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    # user가 데이터를 작성할 때마다 user_id를 FK로 받아 누가 작성했는지 관계를 맺어주면 좋다.
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)     # user id는 Integer로 데이터가 들어오기 때문에 FK로 받을 때도 Integer / FK로 users 테이블에서 id라는 데이터를 가져온다.
    author = db.relationship('User', back_populates='boards')