-- User Stories
-- Each role can do anything the roles below can do.

-- For example, management can do anything a librarian and user can do. However a user can only do what a user can.


-- Management
-- As management, I want to know how many users are registered with the library so that I can assign budgets for the following year.
SELECT count(user_id) FROM person;

-- As management, I want to be able to add specific roles to users so that I can set the permissions accordingly.
UPDATE person SET user_role = '___' WHERE user_id = __;

--  As management, I want to delete a user account;
DELETE FROM person WHERE user_id = __;

-- Librarian
-- As a librarian I want to add books so that they are available to students.
insert into book values(author, title, publisher, published_date, isbn, subject_heading);

-- Add a copy to this book (would need to manually add the accession_id)
insert into copy
values(null, location, classmark, loan_status, accession_id);

-- As a librarian I want to know what books on a topic are available so that we can make more informed future acquisitions.
SELECT * FROM book WHERE subject_heading LIKE '%_____%';

-- As a librarian I want to know what specific books by an author are available so that I can help with a user’s enquiry.
SELECT book.title, book.author, copy.loan_status FROM copy JOIN book ON copy.accession_id = book.accession_id
WHERE book.author LIKE '%____%' AND loan_status = 'Available';

-- As a librarian I want to know the location of a book so that I can find it when needed. (& availability)
SELECT copy.copy_id, copy.location, copy.classmark, copy.loan_status, book.title, book.author
FROM copy
INNER JOIN book ON copy.accession_id=book.accession_id
WHERE copy.accession_id = __;

-- As a librarian I want to know how many copies of a book is in the library so that I can help with a user’s enquiry.
SELECT COUNT(*) FROM copy WHERE accession_id = __;

-- As a librarian I want to see user IDs of users who have books due on particular date.
SELECT user_id FROM loan WHERE date_due = 'yyyy-mm-dd';


-- User
-- As a user I want to find a book on a specific topic so that I can use it for my studies.
SELECT title, author, subject_heading FROM book WHERE subject_heading LIKE '%_____%';

-- As a user I want to know if a book is available so that I can borrow it.
SELECT book.title, book.author, copy.loan_status FROM copy JOIN book ON copy.accession_id = book.accession_id WHERE book.title = '____';

-- As a user I want to borrow a book from the library so that I can read it.
INSERT INTO loan VALUES (null, date_issued, date_due, null, user_id, copy_id);
UPDATE copy  SET loan_status = 'On_loan' WHERE copy_id = __;

-- As a user I want to know when my book is due back to the library so that I can avoid a fine.
SELECT date_due FROM loan WHERE copy_id = __;

-- As a user I want to reserve a book that is currently on loan so that I can get it when it becomes available.
INSERT into reservation
SELECT null, 'yyyy-mm-dd',3, loan.copy_id FROM copy JOIN book ON copy.accession_id = book.accession_id
join loan on loan.copy_id = copy.copy_id
WHERE book.title = '_______' limit 1;-- limit 1 will only bring 1 record back and only reserve 1 copy of the book

-- As a user I want to know the location of the book in the library so that I can retrieve it.
SELECT book.title, book.author, copy.location FROM book JOIN copy on book.accession_id = copy.accession_id 
WHERE book.title = '____';

-- As a user I want to know if I have any fines so that I can pay them off.
SELECT fine_balance FROM person WHERE user_id =__;