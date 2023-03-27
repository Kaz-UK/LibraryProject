-- Test script for logged in library user
use library;
 
-- Student (id=2) checking to see if they have any fines
call CheckFine(2);

-- Student (id=2) looking for a book on Python
select * from book where subject_heading = 'Python (Computer program language)';

-- Student (id=2) looking for any copies of book with accession_id=2
select book.author, book.title, book.publisher, book.published_date, book.subject_heading, copy_id, copies.location, copies.classmark, copies.loan_status from book
inner join copies on book.accession_id=copies.accession_id
where book.accession_id=2;

-- Student (id=2) self issueing book 
call LoanBook('2023-03-27', '2023-04-03', 2, 7);

-- Library users unable to call Get Person Count as they do not have the correct permissions
Call GetPersonCount();