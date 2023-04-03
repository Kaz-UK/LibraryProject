from application import db

# from application import db
# from dataclasses import dataclass
# # the annotation below will help to turn the Python object into a JSON object
# @dataclass
# class Book(db.Model):
#
#     accession_id = db.Column(db.Integer, primary_key=True)
#     author = db.Column(db.String(100), nullable=True)
#     title = db.Column(db.String(300), nullable=False)
#     publisher = db.Column(db.String(100), nullable=True)
#     published_date = db.Column(db.String(10), nullable=True)
#     isbn = db.Column(db.String(15), nullable=True)
#     subject_heading = db.Column(db.String(300), nullable=True)
#     copies = db.relationship('Copy', backref='copies')


# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Book(db.Model):

    accession_id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(300), nullable=False)
    publisher = db.Column(db.String(100), nullable=True)
    published_date = db.Column(db.String(10), nullable=True)
    isbn = db.Column(db.String(15), nullable=True)
    subject_heading = db.Column(db.String(300), nullable=True)
    copies = db.relationship('Copy', backref='copies')
