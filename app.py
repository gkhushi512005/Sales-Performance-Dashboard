import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/superstore.csv", encoding='latin1')

st.title("Retail Sales Dashboard")

total_sales = df['Sales'].sum()

st.metric("Total Revenue", f"${total_sales:,.2f}")

category_sales = df.groupby('Category')['Sales'].sum()

fig = px.bar(
    x=category_sales.index,
    y=category_sales.values,
    title="Sales by Category"
)

st.plotly_chart(fig)
region = st.selectbox(
    "Select Region",
    df['Region'].unique()
)

filtered_df = df[df['Region'] == region]
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100