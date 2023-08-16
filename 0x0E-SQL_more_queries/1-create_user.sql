-- creates a MySQL server for user_0d_1

-- Check if the user user_0d_1 exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_1';

-- Create the user only if it doesn't exist
SET @sql = IF(@user_exists = 0,
    "CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'",
    "SELECT 'User user_0d_1 already exists.' AS Message;"
);

-- Execute the SQL statement for CREATE USER
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
