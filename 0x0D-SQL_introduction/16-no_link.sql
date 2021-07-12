-- Prints score and name (not empty) from second_table in descending order from
--   database passed as argument of the mysql command.
SELECT
	score,
	name
FROM
	second_table
WHERE
	name IS NOT NULL AND
	CHAR_LENGTH(name) > 0
ORDER BY score DESC;
