import sqlite3

import pandas as pd


# Database path
db_path = "data/db/movies.db"

# Load the cleaned dataset
csv_path = "data/processed/movies_clean.csv"
df_movies = pd.read_csv(csv_path)

# Connect to SQLite database
connection = sqlite3.connect(db_path)

# Import the dataset into SQLite
df_movies.to_sql(
    "movies",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Database created successfully.")