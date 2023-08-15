-- this scripts lists all the tables of a database in MySQL server
USE `your_database_name`;

SELECT table_name FROM information_schema.tables WHERE table_schema = 'your_database_name';
