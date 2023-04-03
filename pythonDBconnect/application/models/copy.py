from application import db

# from application import db
# from dataclasses import dataclass
# # the annotation below will help to turn the Python object into a JSON object
# @dataclass
# class Copy(db.Model):
#
#     copy_id = db.Column(db.Integer, primary_key=True)
#     location = db.Column(db.String(50), nullable=False)
#     classmark = db.Column(db.String(10), nullable=True)
#     loan_status = db.Column(db.Integer, nullable=False)
#     books = db.relationship('Book', backref='books')


# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Copy(db.Model):

    copy_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable=False)
    classmark = db.Column(db.String(10), nullable=True)
    loan_status = db.Column(db.Integer, nullable=False)
    accession_id = db.Column(db.Integer, db.ForeignKey('book.accession_id'), nullable=True)
