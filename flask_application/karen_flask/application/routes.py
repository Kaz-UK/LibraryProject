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
    return render_template('home.html', title="Welcome")


# Returns a full list of users, with email details from contacts table
@app.route('/persons', methods=['GET'])
def show_persons():
    error = ""
    contacts = service.get_all_contacts()
    if len(contacts) == 0:
        error = "There is no contact information to display"
    persons_list = []
    for row in contacts:
        person_detail = service.get_person(row.contact_id)
        person_details = {"user_id": person_detail.user_id, "first_name": person_detail.first_name,
                          "surname": person_detail.surname, "email": row.email_address,
                          "library_card": person_detail.library_card}
        persons_list.append(person_details)
    return render_template('persons.html', persons=persons_list, message=error, title="Registered Users")



# Returns a full list of books
@app.route('/books', methods=['GET'])
def show_books():
    error = ""
    books = service.get_all_books()
    if len(books) == 0:
        error = "There are no books to display"
    return render_template('books.html', books=books, message=error, title="Library Holdings")


# Returns a full list of reservations (testing error message as no reservations currently held in database)
@app.route('/reservations', methods=['GET'])
def show_reservations():
    error = ""
    reservations = service.get_all_reservations()
    if len(reservations) == 0:
        error = "There are no reservations to display"
    return render_template('reservations.html', reservations=reservations, message=error, title="Reservations")


# Book by accession id, creates a ReST endpoint (so only returns data)
@app.route('/search_results/<int:accession_id>', methods=['GET'])
def show_book_by_id(accession_id):
    book = service.get_book(accession_id)
    if not book:
        return jsonify(f"There is no book with the Accession ID: {accession_id}")
    else:
        return jsonify(book)


# Book by title, creates a ReST endpoint (so only returns data)
@app.route('/search_results/<string:title>', methods=['GET'])
def copies_from_title(title):
    book = service.get_book_by_title(title)
    if not book:
        return jsonify(f"There is no book with the title '{title}'")
    else:
        copy_list = service.get_copies(book.accession_id)
        return jsonify(book, copy_list)


# Returns a book record and the associated copy records
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
    return render_template('search_author.html', books=book_list, message=error, title="Search Results")


# Returns a book record and the associated copy records
@app.route('/search_subject', methods=['GET'])
def show_search_subject():
    # Unable to collect search term from HTML form so entered here
    search_term = "Python (Computer program language)"
    error = ""
    book_result = service.get_book_by_subject(search_term)
    if len(book_result) == 0:
        error = "There are no books to display"
    book_list = []
    for row in book_result:
        copy_details = service.get_copies(row.accession_id)
        book_details = {"accession_id": row.accession_id, "author": row.author, "title": row.title,
                        "publisher": row.publisher, "published_date": row.published_date, "isbn": row.isbn,
                        "subject_heading": row.subject_heading, "copies": copy_details}
        book_list.append(book_details)
    return render_template('search_subject.html', books=book_list, message=error, title="Search Results")


# Returns a book record and the associated copy records
@app.route('/search_title', methods=['GET'])
def show_search_title():
    # Unable to collect search term from HTML form so entered here
    search_term = "Python"
    error = ""
    book_result = service.get_book_by_title(search_term)
    if len(book_result) == 0:
        error = "There are no books to display"
    book_list = []
    for row in book_result:
        copy_details = service.get_copies(row.accession_id)
        book_details = {"accession_id": row.accession_id, "author": row.author, "title": row.title,
                        "publisher": row.publisher, "published_date": row.published_date, "isbn": row.isbn,
                        "subject_heading": row.subject_heading, "copies": copy_details}
        book_list.append(book_details)
    return render_template('search_title.html', books=book_list, message=error, title="Search Results")


# Returns a full list of loans, with details from loan, person, book tables
@app.route('/loans', methods=['GET'])
def show_loans():
    error = ""
    loans = service.get_all_loans()
    if len(loans) == 0:
        error = "There are no books on loan"
    loans_list = []
    for row in loans:
        loan_detail = service.get_loan_details(row.copy_id)
        person_detail = service.get_loan_user(loan_detail.user_id)
        book_details = service.get_loan_book(row.accession_id)
        loan_details = {"first_name": person_detail.first_name, "surname": person_detail.surname,
                        "title": book_details.title, "date_issued": loan_detail.date_issued,
                        "date_due": loan_detail.date_due, "copy_id": row.copy_id}
        loans_list.append(loan_details)
    # return jsonify(loans_list)
    return render_template('loans.html', loans=loans_list, message=error, title="Loans")
