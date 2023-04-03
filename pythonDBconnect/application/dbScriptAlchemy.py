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
    print("1. Search the catalogue")
    print("2. List all loans")
    print("3. List all reservations")
    print("4. List all users")
    print("5. Add a book record")
    print("6. Add a copy record")
    print("7. Add a user")
    print("\nPress any other key to exit application\n")

    menu = input("What would you like to do? ")

    if menu == "1":
        book_search = input("Please select a subject?: ")
        result = session.query(Book).filter_by(subject_heading=book_search).all()
        for row in result:
            print("")
            print(row.author, row.title, row.publisher, row.published_date, row.isbn, row.subject_heading)
            print("Copies:")
            for b in row.copies:
                print(f"Location: {b.location} -- Classmark: {b.classmark} -- Loan Status: "
                      f"{b.loan_status}")
        print("\n")

    if menu == "2":
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

    if menu == "3":
        result = session.query(Reservation).all()
        for row in result:
            print("")
            copy_result = session.query(Copy).filter_by(copy_id=row.copy_id).first()
            user_result = session.query(Person).filter_by(user_id=row.user_id).first()
            book_reservation = session.query(Book).filter_by(accession_id=copy_result.accession_id).first()
            loan_date = session.query(Loan).filter_by(copy_id=row.copy_id).first()
            print(f"User: {user_result.first_name} {user_result.surname}")
            print(f"Book reservation: {book_reservation.author} {book_reservation.title} "
                  f"{book_reservation.published_date}")
            print(f"Date of reservation: {row.reservation_date}")
            print(f"Current expected date of return: {loan_date.date_due}")

    if menu == "4":
        result = session.query(Contact).all()
        for row in result:
            print("")
            for c in row.persons:
                print(f"User: {c.first_name} {c.surname}\nLibrary card number: {c.library_card}")
                print(f"Address: {row.first_line}\nCity/Town: {row.city_town} \nEmail: "
                      f"{row.email_address}")

    if menu == "5":
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
        session.commit()

    if menu == "6":
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
            add_loan_status = input("Data entry (Loan Status (Available or In processing): ")
            copy_add = Copy(location=add_location, classmark=add_classmark, loan_status=add_loan_status,
                            accession_id=result.accession_id)
            session.add(copy_add)
            session.commit()

    if menu == "7":
        add_first_line = input("Address (first line): ")
        add_second_line = input("Address (second line):  ")
        add_city = input("City/Town: ")
        add_postcode = input("Postcode: ")
        add_email = input("Email: ")
        add_phone = input("Phone: ")
        user_contact = Contact(first_line=add_first_line, second_line=add_second_line, city_town=add_city,
                               postcode=add_postcode, email_address=add_email, phone_number=add_phone)
        session.add(user_contact)
        session.commit()
        # how to auto add to the record created above
        add_to_contact = input("Which email would you like to use for this user? ")
        result = session.query(Contact).filter_by(email_address=add_to_contact).first()
        print(result.email_address)
        add_user_true = input("Is this the correct email for this user? (Y/N) ")
        if add_user_true.lower() == 'y':
            add_first_name = input("Enter first name: ")
            add_surname = input("Enter surname: ")
            add_user_role = input("Enter 'Student', 'Staff' or 'Library Staff': ")
            add_library_card = input("Enter 5 digit library card number: ")
            user_add = Person(first_name=add_first_name, surname=add_surname, user_role=add_user_role,
                              library_card=add_library_card, contact_id=result.contact_id)
            session.add(user_add)
            session.commit()

    library_application = input("\nEnter 'y' to return to the main menu, or any other key to exit ")

print("Thank you for using the library")
