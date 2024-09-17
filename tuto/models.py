

import yaml, os.path
from .app import db

Books = yaml.safe_load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            "data.yml"
        )
    )
)

# Pour avoir un id
i = 0
for book in Books:
    book['id'] = i
    i += 1
    
def get_sample():
    return Books[0:20]

class Author(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    
class Book(db.Models):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float)
    url = db.Column(db.String(200))
    image = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.models.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("books", lazy="dynamic"))
    
    
    