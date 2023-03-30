--  As management, I want to delete a user account;
DELETE FROM person WHERE user_id = 4;

-- update user_roles to whatever you want in CHANGE HERE (management)
UPDATE person SET user_role = 'student' WHERE user_id = 1;

-- As a librarian I want to add books so that they are available to students.
insert into book values('Horstmann, Cay S', 'Python for everyone', 'Wiley', '2019', 9781119498612, 'Python (Computer program language)');

-- Add a copy to this book (would need to manually add the accession_id)
insert into copy
values(null, 'IT Library', '005 HOR', 'Available', 6);

-- As a librarian I want to know what books on a topic are available so that we can make more informed future acquisitions.
SELECT * FROM book WHERE subject_heading LIKE '%Python%';

-- As a librarian I want to know what specific books by an author are available so that I can help with a user’s enquiry.
SELECT book.title, book.author, copy.loan_status FROM copy JOIN book ON copy.accession_id = book.accession_id
WHERE book.author LIKE '%Shakespeare%' AND loan_status = 'Available';

-- As a librarian I want to know the location of a book so that I can find it when needed. (& availability)
SELECT copy.copy_id, copy.location, copy.classmark, copy.loan_status, book.title, book.author
FROM copy
INNER JOIN book ON copy.accession_id=book.accession_id
WHERE copy.accession_id = 1;

-- As a librarian I want to know how many copies of a book is in the library so that I can help with a user’s enquiry.
SELECT COUNT(*) FROM copy WHERE accession_id = 1;

-- As a librarian I want to see user IDs of users who have books due on 2023-03-28.
SELECT user_id FROM loan WHERE date_due = '2023-03-28';

-- As a user I want to find a book on a specific topic so that I can use it for my studies.
SELECT title, author, subject_heading FROM book WHERE subject_heading LIKE '%Python%';

-- As a user I want to know if a book is available so that I can borrow it.
SELECT book.title, book.author, copy.loan_status FROM copy JOIN book ON copy.accession_id = book.accession_id WHERE book.title = 'Romeo and Juliet';

-- As a user I want to borrow a book from the library so that I can read it.
INSERT INTO loan VALUES (null, '2023-03-26', '2023-04-01', null, 1, 3);
UPDATE copy  SET loan_status = 'On loan' WHERE copy_id = 3;

-- As a user I want to know when my book is due back to the library so that I can avoid a fine.
SELECT date_due FROM loan WHERE copy_id = 2;

-- As a user I want to reserve a book that is currently on loan so that I can get it when it becomes available.
INSERT into reservation
SELECT null,'2023-03-25',3, loan.copy_id FROM copy JOIN book ON copy.accession_id = book.accession_id
join loan on loan.copy_id = copy.copy_id
WHERE book.title = 'Programming for computations : Python' limit 1;-- limit 1 will only bring 1 record back and only reserve 1 copy of the book
SELECT * FROM reservation;

-- As a user I want to know the location of the book in the library so that I can retrieve it.
SELECT book.title, book.author, copy.location FROM book JOIN copy on book.accession_id = copy.accession_id 
WHERE book.title = 'Romeo and Juliet';

-- As a user I want to know if I have any fines so that I can pay them off.
SELECT fine_balance FROM person WHERE user_id =1;