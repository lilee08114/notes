
from .extension import db

class Image(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image_path = db.Column(db.String(128), unique=True, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text)