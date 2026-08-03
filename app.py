import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Make the page wider
st.set_page_config(page_title="Dubai Business Analytics", layout="wide")

# Big title
st.title("📊 Dubai Business Trends Dashboard")
st.markdown("---")

# Create fake data (we'll use real data later!)
import datetime
dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
data = {
    'Date': dates,
    'Revenue': np.random.randint(1000, 10000, len(dates)),
    'Customers': np.random.randint(20, 200, len(dates)),
    'Rating': np.random.uniform(3.5, 5.0, len(dates))
}
df = pd.DataFrame(data)

# Show top 5 rows so you know it works
st.subheader("📋 Sample Data")
st.dataframe(df.head())

# Make some cool charts
st.subheader("📈 Revenue Trend")
fig1 = px.line(df, x='Date', y='Revenue', title='Daily Revenue')
st.plotly_chart(fig1)

st.subheader("👥 Customer Distribution")
fig2 = px.histogram(df, x='Customers', title='How many customers visit')
st.plotly_chart(fig2)

# Show summary numbers
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Total Revenue", f"${df['Revenue'].sum():,}")
with col2:
    st.metric("👥 Total Customers", f"{df['Customers'].sum():,}")
with col3:
    st.metric("⭐ Avg Rating", f"{df['Rating'].mean():.2f}")

st.caption("Built with ❤️ by [YOUR NAME] | MDX Dubai")
