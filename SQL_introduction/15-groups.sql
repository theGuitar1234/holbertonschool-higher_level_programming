-- agfsg
SELECT score, COUNT(DISTINCT score) AS number FROM second_table ORDER BY number DESC;
