-- Prints max temperature from the temperatures table grouped and ordered
--   by state from database passed as argument of the mysql command.
SELECT
	state,
	MAX(value) AS max_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY state
ORDER BY state ASC;
