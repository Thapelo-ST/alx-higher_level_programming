-- creates a table 'id_not_null'
-- Set the database name
SET @db_name = 'hbtn_0d_2';

-- Check if the table id_not_null exists in the specified database
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = @db_name AND table_name = 'id_not_null';

-- Create the table only if it doesn't exist
SET @sql = IF(@table_exists = 0,
    CONCAT('CREATE TABLE ', @db_name, '.id_not_null (',
           'id INT NOT NULL DEFAULT 1, ',
           'name VARCHAR(256)',
           ')'
    ),
    ''
);

-- Execute the SQL statement for CREATE TABLE
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
