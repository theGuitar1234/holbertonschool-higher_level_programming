-- kasdhjfkjd
SELECT title FROM tv_shows
WHERE id NOT IN (
    SELECT id FROM tv_genres g1
    JOIN tv_genres g2 ON g1.genre_id = g2.id
    WHERE g1.name = 'Comedy'
)
ORDER BY title;
