import pandas as pd

from logger import logger


def transform(raw_book_data):

    logger.info(
        "Starting Transformation Process"
    )

    try:
        if raw_book_data.empty:

            logger.warning(
                "No data available for transformation"
            )

            return pd.DataFrame()

        cleaned_book_data = raw_book_data.copy()

        cleaned_book_data["price"] = pd.to_numeric(

            cleaned_book_data["price"]

            .astype(str)

            .str.replace(
                r"[^0-9.]",
                "",
                regex=True
            ),

            errors="coerce"

        )

        logger.info(
            "Price column cleaned successfully"
        )

        missing_values = (
            cleaned_book_data.isnull().sum()
        )

        logger.info(
            f"Missing values before cleaning:\n{missing_values}"
        )

        cleaned_book_data.dropna(
            inplace=True
        )

        logger.info(
            "Missing values handled successfully"
        )

        duplicate_count = (
            cleaned_book_data.duplicated().sum()
        )

        logger.info(
            f"Duplicate rows found: {duplicate_count}"
        )

        cleaned_book_data.drop_duplicates(
            inplace=True
        )

        logger.info(
            "Duplicates removed successfully"
        )

        cleaned_book_data.reset_index(
            drop=True,
            inplace=True
        )

        cleaned_book_data.to_csv(
            "data/cleaned_book_data.csv",
            index=False
        )

        logger.info(
            "Cleaned data saved successfully"
        )

        logger.info(
            f"Final Record Count: {len(cleaned_book_data)}"
        )

        return cleaned_book_data

    except Exception as e:

        logger.exception(
            f"Transformation failed: {e}"
        )

        return pd.DataFrame()