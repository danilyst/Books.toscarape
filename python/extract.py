import requests
from bs4 import BeautifulSoup
import pandas as pd
import hashlib
import time

from logger import logger


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

BOOK_BASE_URL = "https://books.toscrape.com/catalogue/"


def get_rating(rating_classes):
    """
    Convert rating text into numeric value.
    """

    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    for key, value in ratings.items():

        if key in rating_classes:
            return value

    return None


def generate_book_id(title):
    """
    Generate unique hash ID.
    """

    return hashlib.md5(
        title.encode()
    ).hexdigest()


def extract():

    logger.info(
        "Starting Extraction Process"
    )

    raw_book_data = []

    # CREATE SESSION
    session = requests.Session()

    headers = {

        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

    }

    try:
        # LOOP THROUGH ALL PAGES
        for page in range(1, 51):

            url = BASE_URL.format(page)

            logger.info(
                f"Scraping Page {page}"
            )

            try:

                response = session.get(
                    url,
                    headers=headers,
                    timeout=10
                )

                response.raise_for_status()

            except Exception as e:

                logger.error(
                    f"Failed to scrape page {page}: {e}"
                )

                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            books = soup.find_all(
                "article",
                class_="product_pod"
            )

            logger.info(
                f"{len(books)} books found on page {page}"
            )

            # LOOP THROUGH BOOKS
            for book in books:
                try:
                    # TITLE
                    title = (
                        book.h3.a["title"]
                    )
                    # PRICE
                    price = (
                        book.find(
                            "p",
                            class_="price_color"
                        )
                        .text
                        .replace("£", "")
                        .strip()
                    )
                    # RATING
                    rating_tag = book.find(
                        "p",
                        class_="star-rating"
                    )
                    rating = get_rating(
                        rating_tag["class"]
                    )                 
                    # BOOK DETAIL URL
                    relative_link = (
                        book.h3.a["href"]
                    )
                    book_url = (
                        BOOK_BASE_URL
                        + relative_link.replace(
                            "../",
                            ""
                        )
                    )
                    # REQUEST DETAIL PAGE
                    try:

                        detail_response = session.get(
                            book_url,
                            headers=headers,
                            timeout=10
                        )

                        detail_response.raise_for_status()

                    except Exception as e:

                        logger.error(
                            f"Failed to access detail page for {title}: {e}"
                        )

                        continue

                    detail_soup = BeautifulSoup(
                        detail_response.text,
                        "html.parser"
                    )
                    # CATEGORY
                    category = (
                        detail_soup.find(
                            "ul",
                            class_="breadcrumb"
                        )
                        .find_all("li")[2]
                        .text
                        .strip()
                    )
                    # BOOK ID
                    book_id = generate_book_id(
                        title
                    )
                    # STORE DATA
                    raw_book_data.append({

                        "book_id": book_id,

                        "title": title,

                        "category": category,

                        "price": price,

                        "rating": rating

                    })

                    logger.info(
                        f"Extracted: {title}"
                    )

                    # DELAY BETWEEN BOOKS
                    time.sleep(1)

                except Exception as e:

                    logger.error(
                        f"Error extracting book: {e}"
                    )

            # DELAY BETWEEN PAGES

            time.sleep(2)

        # HANDLE EMPTY DATA
        if not raw_book_data:

            logger.warning(
                "No books were extracted"
            )

            return pd.DataFrame()

        raw_book_data = pd.DataFrame(
            raw_book_data
        )

        raw_book_data.to_csv(
            "data/raw_book_data.csv",
            index=False
        )

        logger.info(
            "Raw data saved successfully"
        )

        logger.info(
            f"Total Records: {len(raw_book_data)}"
        )

        return raw_book_data

    except Exception as e:

        logger.exception(
            f"Extraction failed: {e}"
        )

        return pd.DataFrame()


if __name__ == "__main__":

    extract()