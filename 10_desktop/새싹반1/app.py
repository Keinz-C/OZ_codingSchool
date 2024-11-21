from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from models import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

# user에 대한 CRUD 작성

db.init_app(app)

migrate = Migrate(app, db)

users = [
    {
        "id": 1, "username": "chicken", "password": "koko"
    },
    {
        "id": 2, "username": "hamburger", "password": "ham"
    },
    {
        "id": 3, "username": "pizza", "password": "치즈"
    },
]
user_count = 3


@app.route('/users/', methods=["GET"])
def index():
    global users
    return render_template("index.html", users=users)


@app.route("/users/<int:user_id>", methods=["GET"])
def user_detail(user_id):
    global users
    user = next(iter([{"username": user["username"], "id": user["id"]} for user in users if user["id"] == user_id]))
    return render_template("detail.html", user=user)


@app.route("/users/register", methods=["GET", "POST"])
def register():
    global users
    global user_count
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_count += 1
        users.append({"id": user_count, "username": username, "password": password})
        return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/users/<int:user_id>/remove", methods=["GET"])
def remove(user_id):
    global users
    for idx, user in enumerate(users):
        if user["id"] == user_id:
            del users[idx]
    return redirect(url_for("index"))


@app.route("/users/<int:user_id>/edit", methods=["POST", "GET"])
def edit_username(user_id):
    global users

    user = None
    for _user in users:
        if _user["id"] == user_id:
            user = _user

    if request.method == "POST":
        username = request.form["username"]
        user["username"] = username
        return redirect(url_for("index"))
    return render_template("edit.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
