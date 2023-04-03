from application import db

# from dataclasses import dataclass
# # # the annotation below will help to turn the Python object into a JSON object
# @dataclass
# class Contact(db.Model):
#
#     contact_id = db.Column(db.Integer, primary_key=True)
#     first_line = db.Column(db.String(50), nullable=False)
#     second_line = db.Column(db.String(10), nullable=True)
#     city_town = db.Column(db.Integer, nullable=False)
#     postcode = db.Column(db.String(10), nullable=False)
#     email_address = db.Column(db.Integer, nullable=True)
#     phone_number = db.Column(db.Integer, nullable=True)
#     persons = db.relationship('Person', backref='persons')


# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Contact(db.Model):

    contact_id = db.Column(db.Integer, primary_key=True)
    first_line = db.Column(db.String(50), nullable=False)
    second_line = db.Column(db.String(10), nullable=True)
    city_town = db.Column(db.Integer, nullable=False)
    email_address = db.Column(db.Integer, nullable=True)
    phone_number = db.Column(db.Integer, nullable=True)
    persons = db.relationship('Person', backref='persons')
