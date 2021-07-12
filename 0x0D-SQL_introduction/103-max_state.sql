-- Prints max temperature from the temperatures table grouped and ordered
--   by state from database passed as argument of the mysql command.
SELECT
	state,
	MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
