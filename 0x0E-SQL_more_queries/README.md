# SQL Script Examples

This repository contains a collection of SQL script examples that cover various tasks and scenarios commonly encountered when working with databases. Each script demonstrates how to perform specific actions using SQL queries. The scripts are written in MySQL syntax and can be used as a reference for learning and practicing SQL.

## Contents

- **Creating Users and Privileges**
  - `1-create_user.sql`: Creates a new MySQL user with all privileges.

- **Creating Tables and Constraints**
  - `3-force_name.sql`: Creates a table with id and name columns, enforcing a NOT NULL constraint on name.
  - `4-never_empty.sql`: Creates a table with id and name columns, setting a default value for id.
  - `5-unique_id.sql`: Creates a table with id and name columns, making id unique with a default value.
  - `6-states.sql`: Creates a table for states with id and name columns, setting id as primary key.
  - `7-cities.sql`: Creates a table for cities with id, state_id, and name columns, using state_id as a foreign key.

- **Querying Data**
  - `8-cities_of_california.sql and 9`: Lists all cities and their corresponding state names from the database.
  - `10-genre_id_by_shows.sql`: Lists all TV show titles and associated genre IDs from the database.
  - `11-genre_id_all_shows.sql`: Lists all TV show titles that are classified as Comedy.
  - `14-dexter_genres.sql`: Lists all genres of the show Dexter from the database.

- **Advanced Querying**
  - `list_genres_with_show_count.sql`: Lists all genres along with the number of linked TV shows.
  - `list_shows_with_genres.sql`: Lists all shows along with their linked genres, displaying NULL for shows without genres.
  - `list_shows_without_genres.sql`: Lists all shows without linked genres, displaying NULL in the genre column.

## Usage

1. Ensure you have a MySQL server installed.
2. Replace `@db_name` with your actual database name in the scripts that require it.
3. Run the scripts using the MySQL command-line tool or a GUI tool like phpMyAdmin.

Feel free to explore, modify, and use these scripts to enhance your understanding of SQL and database management.
