-- Prints top three city temperatures from the temperatures table
--   from database passed as argument of the mysql command.
SELECT
	city,
	AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
