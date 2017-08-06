from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result
from services.scraper import Scraper

@app.route("/")
def index():
    script = Scraper().scrape('alj')
    return script

if __name__ == '__main__':
    app.run()
