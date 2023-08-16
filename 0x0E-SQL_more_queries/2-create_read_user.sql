-- creates database hbtn_0d_2 and user_0d_2
-- Check if the database hbtn_0d_2 exists
SELECT COUNT(*) INTO @db_exists FROM information_schema.schemata WHERE schema_name = 'hbtn_0d_2';

-- Check if the user user_0d_2 exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_2';

-- Create the database only if it doesn't exist
SET @sql_create_db = IF(@db_exists = 0, "CREATE DATABASE hbtn_0d_2;", "");

-- Execute the SQL statement for CREATE DATABASE
PREPARE stmt_create_db FROM @sql_create_db;
EXECUTE stmt_create_db;
DEALLOCATE PREPARE stmt_create_db;

-- Create the user only if it doesn't exist
SET @sql_create_user = IF(@user_exists = 0,
    "CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'",
    ""
);

-- Execute the SQL statement for CREATE USER
PREPARE stmt_create_user FROM @sql_create_user;
EXECUTE stmt_create_user;
DEALLOCATE PREPARE stmt_create_user;

-- Grant SELECT privilege to the user for the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
