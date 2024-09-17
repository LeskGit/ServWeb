from .app import app
from flask import render_template
from .models import get_sample

@app.route ("/")
def home():
    return render_template(
        "home.html",
        title="Hello World")
    
    
@app.route ("/name")
def show_name():
    return render_template(
        "home.html",
        title="name",
        names=["Pierre", "Jean", "Axel"])
    
    
@app.route ("/sample")
def sample():
    return render_template(
        "home.html",
        title="My Books !",
        books=get_sample())
    
    
@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)]
    return render_template(
    "detail.html",
    b=book)