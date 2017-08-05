from cutups import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String())
    titles = db.Column(JSON)

    def __init__(self, date, titles):
        self.date = date
        self.titles = titles

    def __repr__(self):
        return '<id {}>'.format(self.id)
