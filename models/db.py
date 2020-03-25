from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("TLDR")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)


class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer, unique=True, nullable=False)
    topic = db.Column(db.String, unique=True, nullable=False)


#db.session.add(Topics(name="Flask", email="example@example.com"))
print(Topics.query.all())
