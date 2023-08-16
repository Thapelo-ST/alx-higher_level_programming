-- creates a database and uses it to insert the table 'states'

-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Check if the table states exists in the database
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = 'hbtn_0d_usa' AND table_name = 'states';

-- Create the table states only if it doesn't exist
SET @sql = IF(@table_exists = 0,
    'CREATE TABLE states (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        UNIQUE KEY idx_unique_id (id)
    )',
    ''
);

-- Execute the SQL statement for CREATE TABLE
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
