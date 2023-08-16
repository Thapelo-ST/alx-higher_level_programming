-- script creates table 'unique_id' on server hbtn_0d_2
-- Set the database name
SET @db_name = 'hbtn_0d_2';

-- Check if the table unique_id exists in the specified database
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = @db_name AND table_name = 'unique_id';

-- Create the table only if it doesn't exist
SET @sql = IF(@table_exists = 0,
    CONCAT('CREATE TABLE ', @db_name, '.unique_id (',
           'id INT NOT NULL DEFAULT 1, ',
           'name VARCHAR(256), ',
           'PRIMARY KEY (id), ',
           'UNIQUE KEY idx_unique_id (id)',
           ')'
    ),
    ''
);

-- Execute the SQL statement for CREATE TABLE
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
