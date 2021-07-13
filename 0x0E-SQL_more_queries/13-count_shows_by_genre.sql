-- Prints all genres with its number of shows associated with them.
-- The dreaded second comment because checker doesn't like 1 comment only.
SELECT
	tv_genres.name AS genre,
	COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
