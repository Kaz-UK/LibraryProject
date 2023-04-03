from application import db

# from dataclasses import dataclass
# # the annotation below will help to turn the Python object into a JSON object
# @dataclass
# class Person(db.Model):
#
#     user_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=True)
#     surname = db.Column(db.String(50), nullable=False)
#     fine_balance = db.Column(db.Float, nullable=True)
#     user_role = db.Column(db.String(50), nullable=False)
#     library_card = db.Column(db.Integer, nullable=True)
#     contacts = db.relationship('Contact', backref='contacts')


# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Person(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    surname = db.Column(db.String(50), nullable=False)
    fine_balance = db.Column(db.Float, nullable=True)
    user_role = db.Column(db.String(50), nullable=False)
    library_card = db.Column(db.Integer, nullable=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.contact_id'), nullable=True)

