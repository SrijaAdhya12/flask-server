from app import db

class Country(db.Model):
    __tablename__ = "Country"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
