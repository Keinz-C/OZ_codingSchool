from flask import Flask, request, redirect, url_for, render_template


@app.route('/users/', methods=['GET'])
def index():
    global users
    return render_template("index.html", users=users)

@app.route('/users', methods=['GET'])
def user_detail(user_id):
    global users
    user = next(iter([{"username": user["username"], "id": user["id"]} for user in users if user["id"] == user_id]))
    return render_template("detail.html", user=user)

@app.route('/users', methods=['GET', 'POST'])
def register():
    global users
    global user_count
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_count += 1
        users.append({"id": user_count, "username": username, "password": password})
        return redirect(url_for)
    return render_template("register.html")

@app.route('/users', methods=['GET', 'POST'])
def remove(user_id):
    global users
    for idx, user in enumerate(users):
        if user["id"] == user_id:
           del users[idx]
    return redirect(url_for("index"))

@app.route('/users/<int:user_id>/edit', methods=['POST', 'GET'])
def edit_username(user_id):
    global users
    
    import pdb; pdb.set_trace()

    user = None
    for idx, _user in users:
            if _user["id"] == user_id:
                user = _user

    if request.method == "POST":
        username = request.form["username"]

        for idx, user in users:
            if user["id"] == user_id:
                user["username"] = user
        return redirect(url_for("index"))
    
    return render_template("edit.html", user=user)