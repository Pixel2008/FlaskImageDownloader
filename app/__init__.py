from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

f = Flask(__name__)
f.config.from_object(Config)
db = SQLAlchemy(f)
migrate = Migrate(f, db)

from app import routes, models
