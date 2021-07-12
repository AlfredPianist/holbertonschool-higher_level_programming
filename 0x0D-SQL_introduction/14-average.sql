-- Deletes all records with score less than 5 from second_table from
--   database passed as argument of the mysql command.
SELECT
	AVG(score) AS average
FROM
	second_table;
