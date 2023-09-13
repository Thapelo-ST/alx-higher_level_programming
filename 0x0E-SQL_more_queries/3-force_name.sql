-- creates table 'force_name' for database hbtn_0d_2
-- Set the database name
SET @db_name = 'hbtn_0d_2';

-- Check if the table force_name exists in the specified database
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = @db_name AND table_name = 'force_name';

-- Create the table only if it doesn't exist
SET @sql = IF(@table_exists = 0,
    CONCAT('CREATE TABLE ', @db_name, '.force_name (',
           'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ',
           'name VARCHAR(256) NOT NULL'
           ')'
    ),
    ''
);

-- Execute the SQL statement for CREATE TABLE
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
