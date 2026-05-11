from extract import extract
from transform import transform
from load import load_data
from logger import logger
import os

def run_pipeline():
    logger.info("Starting the ETL pipeline")
    
    try:
        raw_book_data = extract()
        logger.info( f"Extracted {len(raw_book_data)} books successfully")

        cleaned_book_data = transform(raw_book_data)
        logger.info("Transformed the data successfully")

        load_data(cleaned_book_data)
        logger.info("Loaded data into PostgreSQL successfully")

    except Exception as e:

        logger.exception(f"ETL Pipeline Failed: {e}")

    logger.info("ETL Pipeline Completed")


if __name__ == "__main__":

    run_pipeline()