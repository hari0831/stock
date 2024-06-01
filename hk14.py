# stock_app.py
import streamlit as st
import yfinance as yf

st.title("Historical Stock Prices")

# User input: stock symbol
stock_symbol = st.text_input("Enter stock symbol (e.g., AAPL):")

if stock_symbol:
    # Fetch historical stock data
    stock_data = yf.download(stock_symbol, start="2020-01-01", end="2021-12-31")

    # Display stock data
    st.dataframe(stock_data)

    # Plot stock prices
    st.line_chart(stock_data["Adj Close"])
