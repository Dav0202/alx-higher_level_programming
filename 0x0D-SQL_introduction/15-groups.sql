--  Lists the number of records with the same score in the table second_table
-- Query to perform operation
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
