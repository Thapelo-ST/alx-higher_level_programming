-- lists all records 'second_table' without rows that are null
SELECT score, name FROM hbtn_0c_0.second_table WHERE name IS NOT NULL ORDER BY score DESC;
