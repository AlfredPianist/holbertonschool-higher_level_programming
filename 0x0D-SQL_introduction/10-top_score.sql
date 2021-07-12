-- Prints score and name of second_table in descending order from database
--   passed as argument of the mysql command.
SELECT
	score,
	name
FROM second_table
ORDER BY score DESC;
