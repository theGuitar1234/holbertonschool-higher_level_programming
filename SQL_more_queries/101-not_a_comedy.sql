-- kasdhjfkjd
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT g1.genre_id FROM tv_genres g1
    JOIN tv_genres g2 ON g1.genre_id = g2.genre_id
    WHERE g1.name = 'Comedy'
)
ORDER BY tv_shows.title;
