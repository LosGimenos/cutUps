from app import db

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String())
    date = db.Column(db.String())
    titles = db.Column(db.String())

    def __init__(self, source, date, titles):
        self.source = source
        self.date = date
        self.titles = titles

    def __repr__(self):
        return '<id {}>'.format(self.id)
