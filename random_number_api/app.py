from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import uuid

app = Flask(__name__)
db = SQLAlchemy()

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(100), nullable=False)
    
    def __init__(self):
        self.key = str(uuid.uuid4())
    
    @classmethod
    def find_by_key(cls, key):
        return cls.query.filter_by(key=key).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

@app.route('/randomNumber/<int(signed=True):min>/<int(signed=True):max>')
def randomNumber(min, max):
    if min >= max:
        return jsonify({"message": "min must be less than max"}), 400
    headers = request.headers
    auth = headers.get("Authorization")

    if Key.find_by_key(auth):
        return jsonify(random.randint(min, max)), 200
    return jsonify({"message": "Unauthorized"}), 401

@app.route('/', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        key = Key()
        key.save_to_db()
        return render_template("index.html", key=key.key)
    return render_template("index.html")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
