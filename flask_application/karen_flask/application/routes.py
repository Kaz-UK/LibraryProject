from flask import render_template, jsonify, request
from application.models.book import Book
from application.models.copy import Copy
from application.models.person import Person
from application.models.contact import Contact
from application.models.loan import Loan
from application.models.reservation import Reservation
from application import app, service


# Creates a homepage using the Jinja template
@app.route('/')
@app.route('/home')
def show_home():
    return render_template('home.html')


# Returns a full list of users
@app.route('/persons', methods=['GET'])
def show_persons():
    error = ""
    persons = service.get_all_persons()
    if len(persons) == 0:
        error = "There are no users to display"
    return render_template('persons.html', persons=persons, message=error)


# Returns a full list of books
@app.route('/books', methods=['GET'])
def show_books():
    error = ""
    books = service.get_all_books()
    if len(books) == 0:
        error = "There are no books to display"
    return render_template('books.html', books=books, message=error)


# Returns a full list of reservations
@app.route('/reservations', methods=['GET'])
def show_reservations():
    error = ""
    reservations = service.get_all_reservations()
    if len(reservations) == 0:
        error = "There are no reservations to display"
    return render_template('reservations.html', reservations=reservations, message=error)


# This works, creates a ReST endpoint (so only returns data)
@app.route('/search_results/<int:accession_id>', methods=['GET'])
def show_book_by_id(accession_id):
    book = service.get_book(accession_id)
    if not book:
        return jsonify(f"There is no book with the Accession ID: {accession_id}")
    else:
        return jsonify(book)


# This works, creates a ReST endpoint (so only returns data)
@app.route('/search_results/<string:title>', methods=['GET'])
def copies_from_title(title):
    book = service.get_book_by_title(title)
    if not book:
        return jsonify(f"There is no book with the title '{title}'")
    else:
        copy_list = service.get_copies(book.accession_id)
        return jsonify(book, copy_list)


# # This is not working, only returns copies for one book
# @app.route('/search_author', methods=['GET'])
# def show_search_author():
#     # Unable to collect search term from HTML form so entered here
#     search_term = "Adams, Ruth"
#     error = ""
#     book_result = service.get_book_by_author(search_term)
#     if len(book_result) == 0:
#         error = "There are no books to display"
#     # This does not collect copies for each book object
#     for book in book_result:
#         copy_result = service.get_copies(book.accession_id)
#     return render_template('search_author.html', books=book_result, copies=copy_result, message=error)


# This appears to be working, but unsure if this is correct use of OOP
@app.route('/search_author', methods=['GET'])
def show_search_author():
    # Unable to collect search term from HTML form so entered here
    search_term = "Adams, Ruth"
    error = ""
    book_result = service.get_book_by_author(search_term)
    if len(book_result) == 0:
        error = "There are no books to display"
    book_list = []
    for row in book_result:
        copy_details = service.get_copies(row.accession_id)
        book_details = {"accession_id": row.accession_id, "author": row.author, "title": row.title,
                        "publisher": row.publisher, "published_date": row.published_date, "isbn": row.isbn,
                        "subject_heading": row.subject_heading, "copies": copy_details}
        book_list.append(book_details)
    return render_template('search_author.html', books=book_list, message=error)
