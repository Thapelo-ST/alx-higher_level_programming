-- Check if the user user_0d_1 exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_1';

-- Create the user only if it doesn't exist
SET @sql = IF(@user_exists = 0,
    "CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'",
    ""
);

-- Execute the SQL statement for CREATE USER
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Show the grants for the user
SHOW GRANTS FOR 'user_0d_1'@'localhost';
