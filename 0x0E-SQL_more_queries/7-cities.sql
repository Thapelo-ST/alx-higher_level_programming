-- creates a table if it doesnt exist and insert a table cities
-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Check if the table cities exists in the database
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = 'hbtn_0d_usa' AND table_name = 'cities';

-- Create the table cities only if it doesn't exist
SET @sql = IF(@table_exists = 0,
    'CREATE TABLE cities (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        FOREIGN KEY (state_id) REFERENCES states(id),
        UNIQUE KEY idx_unique_id (id)
    )',
    ''
);

-- Execute the SQL statement for CREATE TABLE
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
