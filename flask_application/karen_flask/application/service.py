from application.models.book import Book
from application.models.copy import Copy
from application.models.person import Person
from application.models.contact import Contact
from application.models.loan import Loan
from application.models.reservation import Reservation
from application import db


def get_all_persons():
    return db.session.query(Person).all()


def get_all_books():
    return db.session.query(Book).all()


def get_all_reservations():
    return db.session.query(Reservation).all()


def get_book(accession_id):
    return db.session.query(Book).filter_by(accession_id=accession_id).all()


def get_copies(accession_id):
    return db.session.query(Copy).filter_by(accession_id=accession_id).all()


def get_book_by_author(search_term):
    return db.session.query(Book).filter_by(author=search_term).all()


def get_book_by_title(title):
    return db.session.query(Book).filter_by(title=title).all()
