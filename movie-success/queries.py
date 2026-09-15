from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
engine = sqlite3.connect(BASE_DIR / "data" / "db" / "movies.db")

# Get the 10 highest-grossing movies
top10_high_grossing_query = """
SELECT
    title,
    revenue
FROM movies
WHERE revenue IS NOT NULL
ORDER BY revenue DESC
LIMIT 10;
"""

# Get the 10 movies with the highest budget
top10_high_budget_query = """
SELECT
    title,
    budget
FROM movies
WHERE budget IS NOT NULL
ORDER BY budget DESC
LIMIT 10;
"""

# Get the 10 movies with the highest rating
top10_abs_rating_query = """
SELECT
    title,
    vote_average
FROM movies
WHERE vote_average IS NOT NULL
ORDER BY vote_average DESC
LIMIT 10;
"""

# Get the 10 most voted movies
top10_most_voted_query = """
SELECT
    title,
    vote_count
FROM movies
WHERE vote_count IS NOT NULL
ORDER BY vote_count DESC
LIMIT 10;
"""

# Get the 10 movies with the highest relative rating
top10_rel_rating_query = """
SELECT
    title,
    vote_average * log(1 + vote_count) as relative_rating
FROM movies
WHERE vote_average IS NOT NULL and vote_count IS NOT NULL
ORDER BY relative_rating DESC
LIMIT 10;
"""

# Calculate the average revenue
average_revenue_query = """
SELECT 
    avg(revenue) as revenue
FROM movies
WHERE revenue IS NOT NULL and budget IS NOT NULL
"""

# Calculate the average budget
average_budget_query = """
SELECT 
    avg(budget) as budget
FROM movies
WHERE budget IS NOT NULL and revenue IS NOT NULL
"""

# Get movies with both budget and revenue
budget_and_revenue_query = """
SELECT 
    title, 
    budget, 
    revenue
FROM movies
WHERE budget IS NOT NULL and revenue IS NOT NULL
ORDER BY revenue DESC
"""

# Get movies whose revenue is higher than their budget
budget_less_than_revenue_query = """
SELECT 
    title, 
    budget, 
    revenue
FROM movies
WHERE budget IS NOT NULL and revenue IS NOT NULL and budget < revenue
ORDER BY revenue DESC
"""

# Calculate the revenue-to-budget ratio
revenue_budget_ratio_query = """
SELECT 
    *, 
    revenue / budget as revenue_budget_ratio
FROM movies
WHERE budget IS NOT NULL and revenue IS NOT NULL AND budget >= 10000
ORDER BY revenue_budget_ratio DESC
"""

# Get runtime and rating for movies
runtime_and_rating_query = """
SELECT 
    title, 
    runtime, 
    vote_average * log(1 + vote_count) as rating
FROM movies
WHERE runtime IS NOT NULL and vote_average IS NOT NULL and vote_count IS NOT NULL
"""

# Get runtime and revenue for movies
runtime_and_revenue_query = """
SELECT 
    title, 
    runtime, 
    revenue
FROM movies
WHERE runtime IS NOT NULL and revenue IS NOT NULL
"""

# Get rating and revenue for movies
rel_rating_and_revenue_query = """
SELECT 
    title, 
    vote_average * log(1 + vote_count) as rating, 
    revenue
FROM movies
WHERE vote_average IS NOT NULL and revenue IS NOT NULL and vote_count IS NOT NULL
ORDER BY revenue DESC
"""

count_movies_query = """
SELECT count(*) as num_movies
FROM movies;
"""

# Execute all queries

top10_high_grossing = pd.read_sql(top10_high_grossing_query, engine)
#print("\n--- Top 10 highest-grossing movies ---")
#print(top10_high_grossing)

top10_high_budget = pd.read_sql(top10_high_budget_query, engine)
#print("\n--- Top 10 highest-budget movies ---")
#print(top10_high_budget)

top10_abs_rating = pd.read_sql(top10_abs_rating_query, engine)
#print("\n--- Top 10 highest-rated movies ---")
#print(top10_abs_rating)

top10_most_voted = pd.read_sql(top10_most_voted_query, engine)
#print("\n--- Top 10 most-voted movies ---")
#print(top10_most_voted)

top10_rel_rating = pd.read_sql(top10_rel_rating_query, engine)
#print("\n--- Top 10 movies by relative rating ---")
#print(top10_rel_rating)

average_revenue = pd.read_sql(average_revenue_query, engine)
#print("\n--- Average revenue ---")
#print(average_revenue)

average_budget = pd.read_sql(average_budget_query, engine)
#print("\n--- Average budget ---")
#print(average_budget)

budget_and_revenue = pd.read_sql(budget_and_revenue_query, engine)
#print("\n--- Movies with budget and revenue ---")
#print(budget_and_revenue)

budget_less_than_revenue = pd.read_sql(budget_less_than_revenue_query, engine)
#print("\n--- Movies where revenue > budget ---")
#print(budget_less_than_revenue)

revenue_budget_ratio = pd.read_sql(revenue_budget_ratio_query, engine)
#print("\n--- Revenue-to-budget ratio ---")
#print(revenue_budget_ratio)

runtime_and_rating = pd.read_sql(runtime_and_rating_query,engine)
#print("\n--- Runtime and rating ---")
#print(runtime_and_rating)

runtime_and_revenue = pd.read_sql(runtime_and_revenue_query,engine)
#print("\n--- Runtime and revenue ---")
#print(runtime_and_revenue)

rel_rating_and_revenue = pd.read_sql(rel_rating_and_revenue_query, engine)

count_movies = pd.read_sql(count_movies_query,engine)
#print("\n--- Number of movies ---")
#print(count_movies)