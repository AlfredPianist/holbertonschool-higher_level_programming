-- Prints all genres with their respective rating sum.
SELECT
	tv_genres.name,
	SUM(tv_show_ratings.rate) AS rating
FROM tv_show_genres
INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_show_ratings
	ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
