from application import db

from application.models.book import Book
from application.models.copy import Copy
from application.models.person import Person
from application.models.contact import Contact
from application.models.loan import Loan
from application.models.reservation import Reservation


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = 'library_staff'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'Library'


# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLALCHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))

engine = get_connection()
Session = sessionmaker(bind=engine)

session = Session()

library_application = "y"
while library_application.lower() == "y":

    print("\n************ WELCOME TO TEAM 1 LIBRARY: LIBRARY STAFF ACCESS ************\n")
    print("What would you like to do?\n")
    print(" 1. Search the catalogue")
    print(" 2. Issue a book")
    print(" 3. Return a book")
    print(" 4. Add a book and copy record")
    print(" 5. Add a copy to existing book record")
    print(" 6. User details")
    print(" 7. Add a user")
    print(" 8. List all users")
    print(" 9. List all loans")
    print("10. List all reservations")
    print("\nPress any other key to exit application\n")

    menu = input("What would you like to do? ")

    # Search the catalogue (select from BOOK and COPY tables)
    if menu == "1":
        search_application = "y"
        while search_application.lower() == "y":
            print("1. Search by author")
            print("2. Search by title")
            print("3. Search by subject")
            search_menu = input("Please select an option?: ")
            if search_menu == "1":
                search = input("Please enter an author (Surname, Firstname)?: ")
                result = session.query(Book).filter_by(author=search).all()
                for row in result:
                    print("")
                    print(row.author, row.title, row.publisher, row.published_date, row.isbn, row.subject_heading)
                    print("Copies:")
                    for b in row.copies:
                        print(f"Copy ID: {b.copy_id} -- Location: {b.location} -- Classmark: {b.classmark} "
                              f"-- Loan Status: {b.loan_status}")
                print("\n")
            elif search_menu == "2":
                search = input("Please enter a title?: ")
                result = session.query(Book).filter_by(title=search).all()
                for row in result:
                    print("")
                    print(row.author, row.title, row.publisher, row.published_date, row.isbn, row.subject_heading)
                    print("Copies:")
                    for b in row.copies:
                        print(f"Copy ID: {b.copy_id} -- Location: {b.location} -- Classmark: {b.classmark} -- "
                              f"Loan Status: {b.loan_status}")
                print("\n")
            elif search_menu == "3":
                search = input("Please enter a subject?: ")
                result = session.query(Book).filter_by(subject_heading=search).all()
                for row in result:
                    print("")
                    print(row.author, row.title, row.publisher, row.published_date, row.isbn, row.subject_heading)
                    print("Copies:")
                    for b in row.copies:
                        print(f"Copy ID: {b.copy_id} -- Location: {b.location} -- Classmark: {b.classmark} -- "
                              f"Loan Status: {b.loan_status}")
                print("\n")
            else:
                print("Sorry that was not a valid command")
            search_application = input("\nPress 'y' to search again, or any other key to exit: ")

    # Issue a book (insert into LOAN table, update COPY table)
    if menu == "2":
        user_search = input("Enter library card number: ")
        result = session.query(Person).filter_by(library_card=user_search).first()
        print(f"User: {result.first_name} {result.surname}")
        # Copy ID is attached to the book (in place of a barcode)
        copy_search = input("Copy ID details of the item to be be loaned: ")
        copy_result = session.query(Copy).filter_by(copy_id=copy_search).first()
        if copy_result.loan_status == "On loan" or copy_result.loan_status == "In processing":
            print(f"Sorry this book is {copy_result.loan_status}")
        else:
            print(f"Book issued to {result.first_name} {result.surname}")
            date1 = "2023-04-05"
            date2 = "2023-04-16"
            loan_add = Loan(date_issued=date1, date_due=date2, user_id=result.user_id, copy_id=copy_result.copy_id)
            copy_result.loan_status = "On loan"
            session.add(loan_add)
            session.commit()

    # Return a book (update COPY, LOAN tables)
    if menu == "3":
        copy_search = input("Copy ID details of the item to be be returned: ")
        copy_result = session.query(Copy).filter_by(copy_id=copy_search).first()
        if copy_result.loan_status == "Available" or copy_result.loan_status == "In processing":
            print("This book is not currently on loan")
        else:
            loan_result = session.query(Loan).filter_by(copy_id=copy_result.copy_id).first()
            user_result = session.query(Person).filter_by(user_id=loan_result.user_id).first()
            print(f"Book returned from {user_result.first_name} {user_result.surname}")
            date = "2023-04-05"
            loan_result.date_returned = date
            copy_result.loan_status = "Available"
            session.commit()

    # Add a book and associated copy record (insert into BOOK, COPY tables)
    if menu == "4":
        add_author = input("Data entry (Author (format: surname, first name)): ")
        add_title = input("Data entry (Title): ")
        add_publisher = input("Data entry (Publisher): ")
        add_date = input("Data entry (Date): ")
        add_isbn = input("Data entry (ISBN): ")
        add_subject_heading = input("Data entry (Subject Heading): ")
        resource = Book(author=add_author, title=add_title, publisher=add_publisher, published_date=add_date,
                        isbn=add_isbn,
                        subject_heading=add_subject_heading)
        session.add(resource)
        session.flush()
        add_location = input("Data entry (Location): ")
        add_classmark = input("Data entry (Classmark): ")
        add_loan_status = input("Data entry (Loan Status (Available or In processing): ")
        copy_add = Copy(location=add_location, classmark=add_classmark, loan_status=add_loan_status,
                        accession_id=resource.accession_id)
        session.add(copy_add)
        session.commit()

    # Add a copy to an existing book record (select from BOOK table, insert into BOOK table)
    if menu == "5":
        book_search = input("Please search the title you would like to add a copy to?: ")
        result = session.query(Book).filter_by(title=book_search).all()
        for row in result:
            print("")
            print(f"Accession id: {row.accession_id} \nBook details: {row.author}, {row.title}, {row.publisher}, "
                  f"{row.published_date}, {row.isbn}, {row.subject_heading}")
        item_search = input("Enter the accession number to add a copy?: ")
        result = session.query(Book).filter_by(accession_id=item_search).first()
        print(result.author, result.title, result.published_date, result.isbn)
        add_copy_true = input("Is this the correct book? (Y/N) ")
        if add_copy_true.lower() == 'y':
            add_location = input("Data entry (Location): ")
            add_classmark = input("Data entry (Classmark): ")
            add_loan_status = "Available"
            copy_add = Copy(location=add_location, classmark=add_classmark, loan_status=add_loan_status,
                            accession_id=result.accession_id)
            session.add(copy_add)
            session.commit()

    # Find details on a user (select from PERSON, CONTACT, LOAN, COPY, BOOK tables)
    if menu == "6":
        search = input("Please enter the surname of the user?: ")
        result = session.query(Person).filter_by(surname=search).all()
        for name in result:
            print(f"User ID: {name.user_id} * {name.first_name} {name.surname} *")
        user_search = input("Select a User ID?: ")
        find_user_id = session.query(Person).filter_by(user_id=user_search).first()
        find_contact = session.query(Contact).filter_by(contact_id=find_user_id.contact_id).first()
        find_loans = session.query(Loan).filter_by(user_id=find_user_id.user_id).all()
        print(f"User: {find_user_id.first_name} {find_user_id.surname}")
        print(f"Email: {find_contact.email_address}")
        print("Current loans:")
        for user_loan in find_loans:
            copy_details = session.query(Copy).filter_by(copy_id=user_loan.copy_id).first()
            book_details = session.query(Copy).filter_by(accession_id=copy_details.accession_id).first()
            print(f"\tCopy ID: {user_loan.copy_id} -- Book title: {book_details.accession_id} -- "
                  f"Date due: {user_loan.date_due}")

        result = session.query(Contact).all()

    # Add a user (insert into CONTACT, PERSON tables)
    if menu == "7":
        print("ADD NEW USER")
        add_first_line = input("Address (first line): ")
        add_second_line = input("Address (second line):  ")
        add_city = input("City/Town: ")
        add_postcode = input("Postcode: ")
        add_email = input("Email: ")
        add_phone = input("Phone: ")
        user_contact = Contact(first_line=add_first_line, second_line=add_second_line, city_town=add_city,
                               postcode=add_postcode, email_address=add_email, phone_number=add_phone)
        session.add(user_contact)
        session.flush()
        add_first_name = input("Enter first name: ")
        add_surname = input("Enter surname: ")
        add_user_role = input("Enter 'Student', 'Staff' or 'Library Staff': ")
        add_library_card = input("Enter 5 digit library card number: ")
        user_add = Person(first_name=add_first_name, surname=add_surname, user_role=add_user_role,
                          library_card=add_library_card, contact_id=user_contact.contact_id)
        session.add(user_add)
        session.commit()

    # List all registered users (select from CONTACT, PERSON tables)
    if menu == "8":
        result = session.query(Contact).all()
        for row in result:
            print("")
            for c in row.persons:
                print(f"User: {c.first_name} {c.surname}\nLibrary card number: {c.library_card}")
                print(f"Address: {row.first_line}\nCity/Town: {row.city_town} \nEmail: "
                      f"{row.email_address}")

    # List all loans (select from COPY, BOOK, LOAN, PERSON tables)
    if menu == "9":
        result = session.query(Copy).filter_by(loan_status='On loan').all()
        for row in result:
            print("")
            book_result = session.query(Book).filter_by(accession_id=row.accession_id).first()
            person_result = session.query(Loan).filter_by(copy_id=row.copy_id).first()
            print(f"Book: {book_result.author} {book_result.title} {book_result.published_date}")
            print(f"Location: {row.location} {row.classmark} ({row.loan_status})")
            find_user = session.query(Person).filter_by(user_id=person_result.user_id)
            for user in find_user:
                print(f"On loan to: {user.first_name} {user.surname}")

    # List all reservations (select from RESERVATION, COPY, PERSON, BOOK, LOAN tables)
    if menu == "10":
        result = session.query(Reservation).all()
        for row in result:
            print("")
            copy_result = session.query(Copy).filter_by(copy_id=row.copy_id).first()
            user_result = session.query(Person).filter_by(user_id=row.user_id).first()
            book_reservation = session.query(Book).filter_by(accession_id=copy_result.accession_id).first()
            loan_date = session.query(Loan).filter_by(copy_id=row.copy_id).first()
            loan_user = session.query(Person).filter_by(user_id=loan_date.user_id).first()
            print(f"User: {user_result.first_name} {user_result.surname}")
            print(f"Book reservation: {book_reservation.author} {book_reservation.title} "
                  f"{book_reservation.published_date}")
            print(f"Date of reservation: {row.reservation_date}")
            print(f"Currently on loan to user: {loan_user.first_name} {loan_user.surname}")
            print(f"Current expected date of return: {loan_date.date_due}")

    library_application = input("\nEnter 'y' to return to the main menu, or any other key to exit ")

print("Thank you for using the library")
