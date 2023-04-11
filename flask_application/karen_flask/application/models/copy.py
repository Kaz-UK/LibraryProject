from application import db
from dataclasses import dataclass

# the annotation below will help to turn the Python object into a JSON object
@dataclass
class Copy(db.Model):

    copy_id: int
    location: str
    classmark: str
    loan_status: int
    accession_id: int

    copy_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable=False)
    classmark = db.Column(db.String(10), nullable=True)
    loan_status = db.Column(db.Integer, nullable=False)
    accession_id = db.Column(db.Integer, db.ForeignKey('book.accession_id'), nullable=True)
    books = db.relationship('Book', back_populates='copies')
    loans = db.relationship('Loan', back_populates='copies')
