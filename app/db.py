from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(8), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)



