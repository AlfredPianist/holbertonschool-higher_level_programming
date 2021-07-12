-- Prints average temperature by city in descending order from the temperatures
--   table from database passed as argument of the mysql command.
SELECT
	city,
	AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
