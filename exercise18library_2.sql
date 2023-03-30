create database if not exists Library;
-- selecting database to use
use Library;
-- create table for contact
create table contact(
	contact_id smallint not null primary key auto_increment,
    first_line varchar(120) not null,
    second_line varchar(120),
    city_town varchar(60) not null,
    postcode varchar(10) not null,
    email_address varchar(60),
    phone_number bigint );
-- create table for Person
create table person(
	user_id smallint not null primary key auto_increment,
    first_name varchar(50),
    surname varchar(50) not null,
    fine_balance float,
    user_role enum('Student', 'Staff', 'Library Staff') not null,
    library_card smallint,
    contact_id smallint,
    foreign key (contact_id) references contact (contact_id) );
-- create table for book
create table book(
	accession_id smallint not null primary key auto_increment,
    author varchar(100),
    title varchar(300) not null,
    publisher varchar(100),
    published_date varchar(10),
    isbn bigint,
    subject_heading varchar(300) );
-- create table for copy
create table copy(
	copy_id smallint not null primary key auto_increment,
    location varchar(50) not null,
    classmark varchar(10),
    loan_status enum('Available', 'On loan', 'In processing', 'Reserved') not null,
    accession_id smallint not null,
    foreign key (accession_id) references book (accession_id) );
-- create table for loan
create table loan(
	loan_id smallint not null primary key auto_increment,
    date_issued date,
    date_due date,
    date_returned date,
    user_id smallint not null,
    copy_id smallint not null,
    foreign key (user_id) references person (user_id),
    foreign key (copy_id) references copy (copy_id) );
-- create table for reservations
create table reservation(
	reservation_id smallint not null primary key auto_increment,
    reservation_date date,
    user_id smallint not null,
	copy_id smallint not null,
    foreign key (user_id) references person (user_id),
    foreign key (copy_id) references copy (copy_id) );
-- insert data into contact
insert into contact
	values(1, '78 Bombay Street', 'Room B', 'Manchester', 'M9 8LR', 'lucy.flower2@uni.ac.uk', 07087456449),
	(2, '4 Library Road', 'Salford', 'Manchester', 'M2 VO8', 'jerm.mac@uni.ac.uk', 07087475987),
	(3, '56 High Street', 'Kersal', 'Manchester', 'M8 6QT', 'aoif.22@uni.ac.uk', 07087659741),
	(4, '109 Down Lane', 'Kersal', 'Manchester', 'M8 I91', 'jeanny@uni.ac.uk', 07087471846),
	(5, '99 Friars Park', 'Salford', 'Manchester', 'M7 6RT', 'butterfly88@uni.ac.uk', 07087432679);
-- insert into person
insert into person
	values(1, 'Lucy', 'Flower', 0.00, 'Student', 10001, 1),
	(2, 'Maria', 'Schmidt', 0.00, 'Staff', 10002, 5),
    (3, 'Aoife', 'McGuinness', 0.00, 'Library Staff', null, 3),
    (4, 'Jeremy', 'McKay', 0.00, 'Student', 10003, 2),
    (5, 'Jean', 'Saunders', 0.00, 'Student', 10004, 4);
-- insert into book
insert into book
	values(1, 'Parker, James R.', 'Python : an introduction to programming', 'Mercury Learning & Information', '2017', 9781944534653, 'Python (Computer program language)'),
	(2, 'Campesato, Oswald', 'Python 3 for machine learning', 'Mercury Learning & Information', '2020', 9781683924951, 'Python (Computer program language)'),
    (3, 'Shakespeare, William', 'Romeo and Juliet', 'Penguin', '2020', 9780241430873, 'English Literature'), 
    (4, 'Linge, Svein', 'Programming for computations : Python', 'Springer', '2020', 9783030168773, 'Python (Computer program language)'),
    (5, 'Haverbeke, Marijn', 'Eloquent javascript : a modern introduction to programming', 'No Starch Press', '2014', 9781593275846, 'JavaScript (Computer program language)'),
    (6, null, 'Five European sculptors', 'Arno', '1969', null, 'Sculpture, European -- 20th century'),
    (7, 'Ravichandran, Aruna', 'DevOps for digital leaders', 'Apress', '2016', 9781484218426, 'Project management'),
    (8, 'Livingstone, Andrew', 'The ceramics reader', 'Bloomsbury Academic', '2017', 9781472584434, 'Ceramics -- Theory');
-- insert into copy
insert into copy
	values(1, 'Main Library', '005 PAR', 'Available', 1),
    (2, 'IT Library', '005 PAR', 'On loan', 1),
	(3, 'Main Library', '822 SHA', 'Available', 3),
    (4, 'IT Library', '000 LIN', 'On loan', 4),
    (5, 'Main Library', '730 FIV', 'Available', 5),
    (6, 'Art Library', '738 LIV', 'Available', 7),
    (7, 'Main Library', '005 CAM', 'Available', 2),
    (8,  'Main Library', '738 LIV', 'Available', 6),
    (9, 'IT Library', '005 CAM', 'Available', 2),
    (10, 'IT Library', '005 CAM', 'Available', 2);
-- insert into loan
insert into loan
	values (1, '2023-03-16', '2023-03-29', null, 3, 2),
	(2, '2023-03-15', '2023-03-28', null, 4, 4);
-- insert into reservation
insert into reservation
	values(1, '2023-03-16', 1, 2); 
    