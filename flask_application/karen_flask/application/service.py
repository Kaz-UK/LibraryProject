from application.models.book import Book
from application.models.copy import Copy
from application.models.person import Person
from application.models.contact import Contact
from application.models.loan import Loan
from application.models.reservation import Reservation
from application import db


def get_all_contacts():
    return db.session.query(Contact).all()


def get_person(contact_id):
    return db.session.query(Person).filter_by(contact_id=contact_id).first()


def get_all_books():
    return db.session.query(Book).all()


def get_all_reservations():
    return db.session.query(Reservation).all()


def get_book(accession_id):
    return db.session.query(Book).filter_by(accession_id=accession_id).all()


def get_copies(accession_id):
    return db.session.query(Copy).filter_by(accession_id=accession_id).all()


def get_book_by_author(author):
    return db.session.query(Book).filter_by(author=author).all()


def get_book_by_title(title):
    return db.session.query(Book).filter_by(title=title).all()


def get_book_by_subject(subject):
    return db.session.query(Book).filter_by(subject_heading=subject).all()


def get_all_loans():
    return db.session.query(Copy).filter_by(loan_status="On loan").all()


def get_loan_details(copy_id):
    return db.session.query(Loan).filter_by(copy_id=copy_id).first()


def get_loan_user(user_id):
    return db.session.query(Person).filter_by(user_id=user_id).first()


def get_loan_book(accession_id):
    return db.session.query(Book).filter_by(accession_id=accession_id).first()
