from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgres://ifpqmojeoylmmh:c498994ee062217d6428cf0b6c6dcbffcd2bab03a270b8e2eddab4c29c1d2045@ec2-54-235-167-210.compute-1.amazonaws.com:5432/dbi6d7nlegte50")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        main()
