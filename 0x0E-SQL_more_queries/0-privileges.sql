-- lists all privileges of users_0d_1 and 2

SELECT * FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2');
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
