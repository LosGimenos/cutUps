from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random
import os
import datetime
import textwrap

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)

from models import Result
from services.scraper import Scraper

@app.route("/tell-the-tale")
@cross_origin()
def tell_the_tale():
    date = str(datetime.date.today())
    collection = []
    the_tale = {}
    counter = 0
    for instance in Result.query.filter_by(date=date).all():
        ten_words = textwrap.wrap(instance.titles, 50)
        collection += ten_words
    collection = random.sample(collection, len(collection))
    for i in range(0, len(collection) - 4, 23):
        the_tale[counter] = "" + collection[i] + " " + collection[i+3]
        counter += 1
    return jsonify(the_tale)

@app.route("/results", methods=["POST"])
def show_results():
    date = str(datetime.date.today())
    results = {}
    for instance in Result.query.filter_by(date=date).all():
        results[instance.source] = {
            'date': instance.date,
            'titles': instance.titles
        }
    return jsonify(results)

@app.route("/api/v1/bbc", methods=["POST"])
def bbcFetch():
    script = Scraper().scrape('bbc')
    scrape_data = {
        'source': "bbc",
        'date': datetime.date.today(),
        'titles': " ".join(script)
    }
    try:
        result = Result(
            source = scrape_data['source'],
            date = scrape_data['date'],
            titles = scrape_data['titles']
        )
        print(result)
        db.session.add(result)
        db.session.commit()
    except:
        return "Unable to connect to Database"
    return jsonify(scrape_data)

@app.route("/api/v1/nyt", methods=["POST"])
def nytFetch():
    script = Scraper().scrape('nyt')
    result = Result(
        source = "nyt",
        date = datetime.date.today(),
        titles = " ".join(script)
    )
    print(script)
    db.session.add(result)
    db.session.commit()

@app.route("/api/v1/fox", methods=["POST"])
def foxFetch():
    script = Scraper().scrape('fox')
    result = Result(
        source = "fox",
        date = datetime.date.today(),
        titles = " ".join(script)
    )
    db.session.add(result)
    db.session.commit()
    return "202"

@app.route("/api/v1/alj", methods=["POST"])
def aljFetch():
    script = Scraper().scrape('alj')
    result = Result(
        source = "alj",
        date = datetime.date.today(),
        titles = " ".join(script)
    )
    db.session.add(result)
    db.session.commit()
    return "202"

@app.route("/api/v1/cnn", methods=["POST"])
def cnnFetch():
    script = Scraper().scrape('cnn')
    result = Result(
        source = "cnn",
        date = datetime.date.today(),
        titles = " ".join(script)
    )
    db.session.add(result)
    db.session.commit()

if __name__ == '__main__':
    app.run()
