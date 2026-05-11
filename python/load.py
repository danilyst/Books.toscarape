from sqlalchemy import create_engine, text
from config import DB_CONFIG
from logger import logger


def get_engine():

    return create_engine(
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['name']}"
    )

def load_data(cleaned_book_data):

    logger.info("Starting Load Process")

    try:

        engine = get_engine()

        logger.info(
            "Database connection established"
        )

        query = text("""

            INSERT INTO bookstoscrape.books
            (
                book_id,
                title,
                category,
                price,
                rating
            )
                     
            VALUES
            (
                :book_id,
                :title,
                :category,
                :price,
                :rating
            )

            ON CONFLICT (book_id)
            DO NOTHING

        """)

        with engine.begin() as connection:

            for _, row in cleaned_book_data.iterrows():

                connection.execute(

                    query,

                    {
                        "book_id": row["book_id"],
                        "title": row["title"],
                        "category": row["category"],
                        "price": row["price"],
                        "rating": row["rating"]
                    }

                )

        logger.info(
            "Data loaded successfully"
        )

    except Exception as e:

        logger.exception(
            f"Load Process Failed: {e}"
        )