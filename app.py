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
    revenue_budget_ratio,
    runtime_and_rating,
    runtime_and_revenue,
    count_movies
)

st.title("What Makes a Movie Successful?")

st.write(
    "An analysis of movie success based on revenue, budget, ratings and other factors."
)

st.subheader("Dataset overview")

num_movies = count_movies["num_movies"].iloc[0]
st.metric("Number of movies", num_movies)

avg_revenue = average_revenue["revenue"].iloc[0]
avg_budget = average_budget["budget"].iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Movies", f"{num_movies:,}")
col2.metric("Average revenue", f"${avg_revenue:,.0f}")
col3.metric("Average budget", f"${avg_budget:,.0f}")

st.subheader("Runtime vs Revenue")
fig = px.scatter(
    runtime_and_revenue,
    x="runtime",
    y="revenue",
    hover_name="title",
    hover_data={
        "runtime": True,
        "revenue": True
    }
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Budget vs Revenue")
fig = px.scatter(
    budget_and_revenue,
    x="budget",
    y="revenue",
    hover_name="title",
    hover_data={
        "budget": True,
        "revenue": True
    }
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Runtime vs Rating")
fig = px.scatter(
    runtime_and_rating,
    x="runtime",
    y="vote_average",
    hover_name="title",
    hover_data={
        "runtime": True,
        "vote_average": True
    }
)
st.plotly_chart(fig, use_container_width=True)