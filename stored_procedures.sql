-- get amount of users 
DELIMITER //
CREATE PROCEDURE GetPersonCount()
BEGIN 
	SELECT COUNT(*) FROM person;
END //
DELIMITER ;

-- update user role 
DELIMITER //
CREATE PROCEDURE UpdateUserRole(
			IN id smallint, 
            IN roles enum('Student', 'Staff', 'Library Staff')
)
BEGIN 
	UPDATE person SET user_role = roles WHERE user_id = id;
END //
DELIMITER ;

-- add book 
DELIMITER //
CREATE PROCEDURE AddBook(
			IN _author varchar(100),
            IN _title  varchar(300),
            IN _publisher varchar(100),
            IN _publishedDate  varchar(10),
            IN _isbn bigint,
            In _subjectHeading varchar(300)
)
BEGIN 
	INSERT INTO book (author, title, publisher, published_date, isbn, subject_heading) VALUES (_author, _title, _publisher, _publishedDate, _isbn, _subjectHeading);
END //
DELIMITER ;

-- check fine balance of a user 
DELIMITER //
CREATE PROCEDURE CheckFine(
			IN id smallint
)
BEGIN 
	SELECT fine_balance FROM person WHERE user_id =id;
END //
DELIMITER ;

-- check amount of copies of a book
DELIMITER //
CREATE PROCEDURE AmountOfCopies(
			IN id smallint
)
BEGIN 
	SELECT COUNT(*) FROM copies WHERE accession_id = id;
END //
DELIMITER ;

-- find book location 
DELIMITER //
CREATE PROCEDURE FindLocation(
			IN id smallint
)
BEGIN 
	SELECT location FROM copies WHERE accession_id = id;
END //
DELIMITER ;

-- check book availability 
DELIMITER //
CREATE PROCEDURE CheckAvailability(
			IN id smallint
)
BEGIN 
	SELECT loan_status FROM copies WHERE accession_id = id;
END //
DELIMITER ;

-- loan a book
DELIMITER //
CREATE PROCEDURE LoanBook(
			IN _date_issued date,
            IN _date_due date,
            IN _user_id smallint, 
            IN _copy_id smallint
)
BEGIN 
	INSERT INTO loans (date_issued, date_due, user_id, copy_id) VALUES (_date_issued, _date_due, _user_id, _copy_id);
	UPDATE copies  SET loan_status = 'On loan' WHERE copy_id = _copy_id;
END //
DELIMITER ;

-- find by author
DELIMITER //
CREATE PROCEDURE FindAuthor(
			IN _author varchar(100)
)
BEGIN 
	SELECT * FROM book WHERE author LIKE CONCAT('%',_author,'%');
END //
DELIMITER ;

-- find by subject
DELIMITER //
CREATE PROCEDURE FindSubject(
			IN _subject varchar(300)
)
BEGIN 
	SELECT * FROM book WHERE subject_heading LIKE CONCAT('%',_subject,'%');
END //
DELIMITER ;

– find copy availability and location
DELIMITER //
CREATE PROCEDURE FindCopies(
			IN id smallint
)
BEGIN 
	SELECT copies.copy_id, copies.location, copies.classmark, copies.loan_status, book.title, book.author
	FROM copies
	INNER JOIN book ON copies.accession_id=book.accession_id
	WHERE copies.accession_id = 1;
END //
DELIMITER ;

– Reserve a book
DELIMITER //
CREATE PROCEDURE ReserveBook(
			IN _reservation_date date,
            IN _user_id smallint, 
            IN _copy_id smallint
)
BEGIN 
	INSERT INTO reservations (reservation_date, user_id, copy_id) VALUES (_reservation_date, _user_id, _copy_id);
END //
DELIMITER ;