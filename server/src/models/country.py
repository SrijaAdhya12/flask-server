
from src import db
from src.models import country_table_name


class Country(db.Model):
    __tablename__ =  country_table_name

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)


