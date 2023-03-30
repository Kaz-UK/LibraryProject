-- create user for general public wanting to browse the database (not a registered user so not logging in)
create user 'opac_user'@'localhost' identified by 'p@$$word';
grant select on library.book to 'opac_user'@'localhost';
grant select on library.copy to 'opac_user'@'localhost';
grant select on library.*;
-- create library user for registered users
create user 'library_user'@'localhost' identified by 'p@$$word';
grant select on library.book to 'library_user'@'localhost';
grant select on library.copy to 'library_user'@'localhost';
grant select on library.loan to 'library_user'@'localhost';
grant select on library.reservation to 'library_user'@'localhost';
-- to allow library user to be able to self issue a book
grant insert (date_issued) on library.loans to 'library_user'@'localhost';
-- to allow library user to be able to reserve a book
grant insert on library.reservation to 'library_user'@'localhost';
-- grant access to procedures
grant execute on procedure CheckFine to 'library_user'@'localhost';
grant execute on procedure LoanBook to 'library_user'@'localhost';
grant execute on procedure CheckAvailability to 'library_user'@'localhost';
grant execute on procedure AmountOfCopies to 'library_user'@'localhost';
grant execute on procedure FindLocation to 'library_user'@'localhost';

-- create library staff user, able to access database to modify data
create user 'library_staff'@'localhost' identified by 'p@$$word';
grant select on library.* to 'library_staff'@'localhost';
grant insert on library.* to 'library_staff'@'localhost';
grant update on library.* to 'library_staff'@'localhost';
-- grant access to procedures
grant execute on procedure GetPersonCount to 'library_staff'@'localhost';
grant execute on procedure AddBook to 'library_staff'@'localhost';
grant execute on procedure FindLocation to 'library_staff'@'localhost';
grant execute on procedure AmountOfCopies to 'library_staff'@'localhost';
grant execute on procedure CheckAvailability to 'library_staff'@'localhost';
grant execute on procedure CheckFine to 'library_staff'@'localhost';

-- create administrator (management) user, able to access database to modify and delete data
create user 'administrator'@'localhost' identified by 'p@$$word';
grant select on library.* to 'administrator'@'localhost';
grant insert on library.* to 'administrator'@'localhost';
grant update on library.* to 'administrator'@'localhost';
grant delete on library.book to 'administrator'@'localhost';
grant delete on library.copy to 'administrator'@'localhost';
-- grant access to procedures
grant execute on procedure GetPersonCount to 'administrator'@'localhost';
grant execute on procedure AddBook to 'administrator'@'localhost';
grant execute on procedure FindLocation to 'administrator'@'localhost';
grant execute on procedure AmountOfCopies to 'administrator'@'localhost';
grant execute on procedure CheckAvailability to 'administrator'@'localhost';
grant execute on procedure CheckFine to 'administrator'@'localhost';
grant execute on procedure UpdateUserRole to 'administrator'@'localhost';
