-- lists all shows contained in the database hbtn_0d_tvshows
-- Set the database name
SET @db_name = 'hbtn_0d_tvshows';

-- List all shows with their associated genre IDs (or NULL if no genre)
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, genre_id ASC;
