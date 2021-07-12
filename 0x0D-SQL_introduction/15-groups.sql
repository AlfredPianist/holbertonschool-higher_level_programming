-- Prints the score and its cound by descending order from second_table from
--   database passed as argument of the mysql command.
SELECT
	score,
	COUNT(*) AS number
FROM
	second_table
GROUP BY score
ORDER BY number DESC;
