-- calling the UpdateUseRole stored procedure to update user id = 1 role to 'Staff'
CALL UpdateUserRole(1, 'Staff');
SELECT * FROM person;


-- callng the AddBook stored procedure to add a new book
CALL AddBook ('Price, Ciara', 'How to code 101', 'Mousa Aljasem', 2023, 978328392392, 'Computer Science');
SELECT * FROM book;


-- calling the CheckFine stored procedure to check the fine balance of user id = 1
CALL CheckFine(1);
SELECT user_id, fine_balance FROM person;


-- calling FindSubject stored procedure to find books about Python
CALL FindSubject('python');
SELECT title, subject_heading FROM book;


-- calling CheckAvailability stored procedure to check availability of accession_id  = 2
CALL CheckAvailability (2);
SELECT * FROM copies;