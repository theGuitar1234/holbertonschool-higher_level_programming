-- agfsg
SELECT score, COUNT(DISTINCT score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
