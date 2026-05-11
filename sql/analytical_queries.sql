/*
  Analytical Queries for Book Price Analysis
- Which products are overpriced or underpriced? 
- Which categories show price variation? 
- How do prices change over time? 
- What insights can be derived? 
*/  

-- Which products are overpriced or underpriced?

SELECT
    title,
    category,
    price,
    ROUND(
        AVG(price) OVER (
            PARTITION BY category
        ),
        2
    ) AS category_average_price,
    CASE
        WHEN price >
        AVG(price) OVER (
            PARTITION BY category
        )
        THEN 'Overpriced'
        WHEN price <
        AVG(price) OVER (
            PARTITION BY category
        )
        THEN 'Underpriced'
        ELSE 'Average'
    END AS price_status

FROM bookstoscrape.books
ORDER BY category, price DESC;

-- Which categories show price variation?
SELECT
    category,
    COUNT(*) AS book_count,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(STDDEV(price), 2) AS price_stddev
FROM bookstoscrape.books
GROUP BY category
ORDER BY price_stddev DESC;

-- How do prices change over time?
SELECT
    DATE(loaded_at) AS load_date,
    COUNT(*) AS book_count,
    ROUND(AVG(price), 2) AS average_price
FROM bookstoscrape.books
GROUP BY load_date
ORDER BY load_date;
