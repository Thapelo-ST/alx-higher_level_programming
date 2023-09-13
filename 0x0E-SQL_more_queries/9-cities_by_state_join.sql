-- lists all cities contained in database htbn_0d_usa
-- Set the database name
SET @db_name = 'hbtn_0d_usa';

-- List all cities with their IDs, names, and corresponding state names
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
