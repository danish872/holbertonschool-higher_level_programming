-- lists all records of the table second_table of the database hbtn_0c_0
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
INSERT INTO second_table(score, name) VALUES (18, 'Aria'), (12, 'Aria');
