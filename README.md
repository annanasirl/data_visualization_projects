# What Makes a Movie Successful?

An exploratory data analysis project investigating which factors are associated with movie success, focusing on revenue, budget, ratings, runtime, and audience engagement.

The project uses Python, pandas, SQL, Plotly, and Streamlit to clean, analyse, and visualize data from more than 45,000 movies.

## Dataset

The project is based on [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) by Rounak Banik.

The following variables were selected from the original dataset:

- `title`
- `release_date`
- `genres`
- `budget`
- `revenue`
- `runtime`
- `original_language`
- `vote_average`
- `vote_count`

The data was cleaned to handle missing values, duplicate records, and invalid zero values before being stored in a SQLite database.

## Analysis

The application explores the following questions:

- Which movies have generated the highest revenues?
- Which movies had the highest production budgets?
- Which movies have the highest ratings?
- Which movies have received the most votes?
- Is there a relationship between production budget and revenue?
- Is there a relationship between runtime and revenue?
- How are budget and revenue distributed?
- Which movies have the highest revenue-to-budget ratios?

The analysis distinguishes between revenue exceeding production budget and actual profitability, since production budget alone does not account for marketing, distribution, and other costs.

## Technologies

- Python
- pandas
- SQLite
- SQL
- Plotly
- Streamlit
