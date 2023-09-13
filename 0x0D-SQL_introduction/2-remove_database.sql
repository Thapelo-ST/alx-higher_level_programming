-- this script deletes the database 'htbn_Oc_O without failing if it doesnt exist'
SET @db_name := 'hbtn_0c_0';
SET @drop_sql := NULL;

-- drop database statement if database htbn_Oc_O
IF EXISTS (SELECT schema_name FROM information_schema.schemata WHERE schema_name = @db_name) THEN
    SET @drop_sql := CONCAT('DROP DATABASE ', @db_name);
END IF;

-- drop if it was createdi
IF @drop_sql IS NOT NULL THEN
    PREPARE stmt FROM @drop_sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END IF;
