import streamlit as st
import plotly.express as px
from queries import (
    top10_high_grossing,
    top10_high_budget,
    top10_abs_rating,
    top10_most_voted,
    top10_rel_rating,
    average_revenue,
    average_budget,
    budget_and_revenue,
    budget_less_than_revenue,
    revenue_budget_ratio,
    runtime_and_rating,
    rel_rating_and_revenue,
    runtime_and_revenue,
    count_movies
)

st.set_page_config(page_title="What Makes a Movie Successful?", layout="wide")
st.markdown("""
<style>
    .block-container 
    {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    div[data-testid="stMetricLabel"] 
    {
        font-size: 0.9rem;
    }

    h2 
    {
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("What Makes a Movie Successful?")
st.markdown(
    "An analysis of movie success based on revenue, budget, ratings and other factors. "
    "Using [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)"
)
st.subheader("Dataset overview")

num_movies = count_movies["num_movies"].iloc[0]
profitable_movies = len(budget_less_than_revenue)
movies_with_bv = len(budget_and_revenue)
avg_revenue = average_revenue["revenue"].iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Movies", f"{num_movies:,}")
col2.metric("With budget & revenue", f"{movies_with_bv:,}")
col3.metric("Revenue > budget", f"{profitable_movies:,}")
col4.metric("Average revenue", f"${avg_revenue / 1_000_000:.1f}M")

col1, col2= st.columns(2)

with col1:
    st.subheader("Runtime vs Revenue")
    fig = px.scatter(
        runtime_and_revenue,
        x="runtime",
        y="revenue",
        hover_name="title",
        labels={
            "runtime": "Runtime (minutes)",
            "revenue": "Revenue ($)"
        },
        hover_data={
            "runtime": True,
            "revenue": True
        }
    )
    st.plotly_chart(fig, width='stretch')

with col2:
    st.subheader("Budget vs Revenue")
    fig = px.scatter(
        budget_and_revenue,
        x="budget",
        y="revenue",
        hover_name="title",
        labels={
            "budget": "Budget ($)",
            "revenue": "Revenue ($)"
        },
        hover_data={
            "budget": True,
            "revenue": True
        }
    )
    st.plotly_chart(fig, width='stretch')

col3, col4= st.columns(2)

with col3:
    st.subheader("Rating vs Revenue")
    fig = px.scatter(
        rel_rating_and_revenue,
        x="rating",
        y="revenue",
        hover_name="title",
        labels={
            "rating": "Relative Rating: average of all votes * log(1 + number of votes)",
            "revenue": "Revenue ($)"
        },
        hover_data={
            "rating": True,
            "revenue": True
        }
    )
    st.plotly_chart(fig, width='stretch')

with col4:
    st.subheader("Rating vs Runtime")
    fig = px.scatter(
        runtime_and_rating,
        x="rating",
        y="runtime",
        hover_name="title",
        labels={
            "rating": "Relative Rating: average of all votes * log(1 + number of votes)",
            "runtime": "Runtime (min)"
        },
        hover_data={
            "rating": True,
            "runtime": True
        }
    )
    st.plotly_chart(fig, width='stretch')

st.subheader("Top 10 movies")
col1, col2 = st.columns(2)

with col1:
    st.write("Highest-grossing movies")

    top10r_display = top10_high_grossing.copy()
    top10r_display["revenue"] = (top10r_display["revenue"] / 1_000_000).round(1)
    top10r_display = top10r_display.rename(columns={"title": "Title"})
    top10r_display = top10r_display.rename(columns={"revenue": "Revenue (M$)"})
    st.dataframe(
        top10r_display,
        hide_index=True,
        width='stretch'
    )

with col2:
    st.write("Highest-budget movies")

    top10b_display = top10_high_budget.copy()
    top10b_display["budget"] = (top10b_display["budget"] / 1_000_000).round(1)
    top10b_display = top10b_display.rename(columns={"title": "Title"})
    top10b_display = top10b_display.rename(columns={"budget": "Budget (M$)"})
    st.dataframe(
        top10b_display,
        hide_index=True,
        width='stretch'
    )

col3, col4, col5 = st.columns(3)

with col3:
    st.write("Highest rated movies (Absolute Rating: average of all votes)")
    top10rated_display = top10_abs_rating.copy()
    top10rated_display = top10rated_display.rename(columns={"title": "Title"})
    top10rated_display = top10rated_display.rename(columns={"vote_average": "Absolute Rating"})
    st.dataframe(
        top10rated_display,
        hide_index=True,
        width='stretch'
    )

with col4:
    st.write("Highest rated movies (Relative Rating: average of all votes * log(1 + number of votes))")
    top10ratedr_display = top10_rel_rating.copy()
    top10ratedr_display = top10ratedr_display.rename(columns={"title": "Title"})
    top10ratedr_display = top10ratedr_display.rename(columns={"relative_rating": "Relative Rating"})
    st.dataframe(
        top10ratedr_display,
        hide_index=True,
        width='stretch'
    )

with col5:
    st.write("Most voted movies")
    top10v_display = top10_most_voted.copy()
    top10v_display = top10v_display.rename(columns={"title": "Title"})
    top10v_display = top10v_display.rename(columns={"vote_count": "Number of votes"})
    st.dataframe(
        top10v_display,
        hide_index=True,
        width='stretch'
    )

st.subheader("Budget and revenue distributions")
col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        budget_and_revenue,
        x="budget",
        nbins=500,
        labels={"budget": "Budget ($)"}
    )
    fig.update_layout(
        xaxis_tickformat="~s"
    )
    st.plotly_chart(fig, width='stretch')

with col2:
    fig = px.histogram(
        budget_and_revenue,
        x="revenue",
        nbins=500,
        labels = {"revenue": "Revenue ($)"}
    )
    fig.update_layout(
        xaxis_tickformat="~s"
    )
    st.plotly_chart(fig, width='stretch')

st.subheader("Revenue-to-budget ratio")

st.caption("Movies with a reported budget of at least $10,000. The ratio compares worldwide revenue with production budget.")

ratio_display = revenue_budget_ratio[
    [
        "title",
        "release_date",
        "runtime",
        "original_language",
        "vote_average",
        "revenue_budget_ratio"
    ]
].copy()

ratio_display["revenue_budget_ratio"] = (
    ratio_display["revenue_budget_ratio"].round(1)
)

ratio_display.columns = [
    "Title",
    "Release date",
    "Runtime (min)",
    "Language",
    "Rating",
    "Revenue / Budget"
]

st.dataframe(
    ratio_display,
    hide_index=True,
    width="stretch"
)