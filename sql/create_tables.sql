CREATE SCHEMA IF NOT EXISTS bookstoscrape;

CREATE TABLE IF NOT EXISTS bookstoscrape.books (

    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT,
    price NUMERIC,
    rating FLOAT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);