-- Updates Bob's score to 10 on second_table from database passed
--   as argument of the mysql command.
UPDATE second_table
SET
	score = 10
WHERE name = 'Bob';
