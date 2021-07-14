-- Prints all titles with no "Comedy" genre.
SELECT
	tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN
(
	SELECT
		tv_shows.title
	FROM
		tv_show_genres
	INNER JOIN tv_genres
		ON tv_show_genres.genre_id = tv_genres.id
	INNER JOIN tv_shows
		ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
