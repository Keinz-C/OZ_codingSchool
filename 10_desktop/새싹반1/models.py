from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password_hash = db.Column(db.String(200))

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password=password)

    def check_password_hash(self, password):
        return check_password_hash(pwhash=self.password_hash, password=password)