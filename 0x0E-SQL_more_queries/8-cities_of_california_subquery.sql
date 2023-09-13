-- lists all cities of Calafonia that are in htbn_0d_usa
-- Set the database name
SET @db_name = 'hbtn_0d_usa';

-- List all cities of California sorted by cities.id
SELECT * FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
) ORDER BY id ASC;
