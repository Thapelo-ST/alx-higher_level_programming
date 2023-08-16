-- this script ists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- Set the database name
SET @db_name = 'hbtn_0d_tvshows';

-- List all shows with linked genres (or NULL if no genre)
SELECT tv_shows.title, COALESCE(tv_genres.name, NULL) AS genre FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title ASC, genre ASC;
