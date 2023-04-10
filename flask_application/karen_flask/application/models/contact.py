from application import db
from dataclasses import dataclass

# the annotation below will help to turn the Python object into a JSON object
@dataclass
class Contact(db.Model):

    contact_id: int
    first_line: str
    second_line: str
    city_town: str
    postcode: str
    email_address: int
    phone_number: int

    contact_id = db.Column(db.Integer, primary_key=True)
    first_line = db.Column(db.String(50), nullable=False)
    second_line = db.Column(db.String(10), nullable=True)
    city_town = db.Column(db.Integer, nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    email_address = db.Column(db.Integer, nullable=True)
    phone_number = db.Column(db.Integer, nullable=True)
    persons = db.relationship('Person', back_populates="contacts")
