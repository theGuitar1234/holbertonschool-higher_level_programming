-- askfhkjds
SELECT tv_genres.name, IFNULL(SUM(tv_show_ratings.rate), 0) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings
    ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
