import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, types

# Load database credentials from the .env file
load_dotenv()

# Create a connection to the PostgreSQL database
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Create the movies table if it does not exist
create_table_query = """
CREATE TABLE IF NOT EXISTS movies (
    id TEXT,
    title TEXT,
    release_date DATE,
    genres TEXT,
    budget NUMERIC,
    revenue NUMERIC,
    runtime NUMERIC,
    original_language TEXT,
    vote_average NUMERIC,
    vote_count NUMERIC
);
"""

with engine.connect() as connection:
    connection.execute(text(create_table_query))
    connection.commit()

# Load the cleaned dataset
csv_path = "data/processed/movies_clean.csv"
df_movies = pd.read_csv(csv_path)

# Clear the table before importing the dataset
with engine.connect() as connection:
    connection.execute(text("TRUNCATE TABLE movies"))
    connection.commit()

# Import the cleaned dataset into PostgreSQL
df_movies.to_sql(
    "movies",
    engine,
    if_exists="replace",
    index=False,
    dtype={
        "id": types.Text(),
        "title": types.Text(),
        "release_date": types.Date(),
        "genres": types.Text(),
        "budget": types.Numeric(),
        "revenue": types.Numeric(),
        "runtime": types.Numeric(),
        "original_language": types.Text(),
        "vote_average": types.Numeric(),
        "vote_count": types.Numeric()
    }
)