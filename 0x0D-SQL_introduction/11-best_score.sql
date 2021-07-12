-- Prints score and name of second_table in descending order only records where
--   score is greater or equal than 10 from database passed as argument of the
--   mysql command.
SELECT
	score,
	name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
