from application import db
from dataclasses import dataclass

# # the annotation below will help to turn the Python object into a JSON object
@dataclass
class Loan(db.Model):

    loan_id: int
    date_issued: str
    date_due: str
    date_returned: str

    loan_id = db.Column(db.Integer, primary_key=True)
    date_issued = db.Column(db.String(10), nullable=True)
    date_due = db.Column(db.String(10), nullable=True)
    date_returned = db.Column(db.String(10), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('person.user_id'), nullable=False)
    copy_id = db.Column(db.Integer, db.ForeignKey('copy.copy_id'), nullable=False)
