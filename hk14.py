import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Set up the title and the sidebar
st.title("Historical Stock Prices")
st.sidebar.header("Stock Input")

# User input: stock symbol
stock_symbol = st.sidebar.text_input("Enter stock symbol (e.g., AAPL):")

# User input: date range
start_date = st.sidebar.date_input("Start date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End date", value=pd.to_datetime("2021-12-31"))

if stock_symbol:
    # Validate the dates
    if start_date < end_date:
        # Fetch historical stock data
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        
        if not stock_data.empty:
            # Display stock data
            st.subheader(f"Displaying data for {stock_symbol}")
            st.dataframe(stock_data)

            # Plot stock prices
            st.line_chart(stock_data["Adj Close"])
        else:
            st.error(f"No data found for {stock_symbol} within the given date range.")
    else:
        st.error("Error: End date must fall after start date.")
