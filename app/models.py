from app import db


class EURUSD(db.Model):
    __tablename__ = 'EURUSD'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    open = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    high = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    low = db.Column(db.Numeric(precision=7, scale=5 ), nullable=False)
    close = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    volume = db.Column(db.Integer, nullable=False)