from flask import Flask, render_template, url_for, request, redirect, flash
from email_validator import validate_email, EmailNotValidError
import logging

app = Flask(__name__)
app.config["SECRET_KEY"] = "2AHDHjsajh2308238328"       # config는 기본설정이라는 의미이다.
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def index():
    return 'Hello oz'

@app.route('/hello/<name>', methods=['GET'], endpoint='hello-oz-points')    # endpoint 정의된 함수명을 임의의 별명으로 붙여주는 기능이다.
def hello(name):
    return f'Welcome back {name}'

@app.route('/name/<name>')      # <>의 내용이 변수가 된다.
def show_name(name):
    return render_template("contact.html", name=name)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=['GET', 'POST'])
def contact_complete():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # 입력 정보 체크
        is_valid = True

        if not name:
            flash("사용자명은 필수로 입력해주세요")
            is_valid = False
        
        if not email:
            flash("메일 주소는 필수로 입력해주세요")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("사용자명은 필수로 입력해주세요")
            is_valid = False
        
        if not message:
            flash("문의 내용은 필수로 입력해주세요")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))

        return redirect(url_for("contact_complete"))
    flash("문의해 주셔서 감사합니다.")
    
    return render_template("contact_complete.html")

with app.test_request_context():        # with은 포함된 코드에만 적용되는 인스턴스 같은 것이다.
    print(url_for("index"))
    print(url_for("hello-oz-points", name="sony"))