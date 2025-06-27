-- lists all records with a score >= 10 in the table second_table
SELECT score, name
FROM second_table
WHERE SCORE >= 10
ORDER BY score DESC;
