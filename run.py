from flask import Flask
from flask import request
from flask import render_template
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from gnewsclient import gnewsclient
#from .models import db, Topic


app = Flask('TLDR')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    TOPIC_NAME = db.Column(db.String, unique=True, nullable=False)

#db.session.add(Topics(name="Flask", email="example@example.com"))

@app.route("/")
def home():

    print(Topics.query.all())
    return render_template("index.html")
    
@app.route("/search-topic")
def searchTopic():
    topic = request.args['topic']
    data = "Nothing to say"
    if (topic == 'tech'):
        data = "The latest news in tech is blah blah blah"
    else:
        data = "Please select a valid topic"
    return render_template('index.html/', data=data)

if __name__ == "__main__":      
    app.run(debug=True)
