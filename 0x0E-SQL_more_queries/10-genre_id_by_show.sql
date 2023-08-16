-- from an imported database, this script lists all shows that are in hbtn_0d_tvshows that are atleast linked by one genre
-- Set the database name
SET @db_name = 'hbtn_0d_tvshows';

-- List all shows with at least one linked genre
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
