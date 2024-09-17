from .app import app
import tuto.views
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy (app)