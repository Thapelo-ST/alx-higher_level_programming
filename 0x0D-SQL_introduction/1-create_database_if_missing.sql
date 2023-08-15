-- creates database in MySQL without the use of SELECT or SHOW
SET @db_name := 'hbtn_0c_0';
SET @create_sql := NULL;

-- create if it doesnt exist
IF NOT EXISTS (SELECT schema_name FROM information_schema.schemata WHERE schema_name = @db_name) THEN
    SET @create_sql := CONCAT('CREATE DATABASE ', @db_name);
END IF;

-- create statement if it was built
IF @create_sql IS NOT NULL THEN
    PREPARE stmt FROM @create_sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END IF;
