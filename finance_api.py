import yfinance as yf
import pandas as pd

### ✅ Task 1: Fetch Basic Stock Data ###
def fetch_stock_data():
    stocks = input("Enter at least two stock symbols separated by commas: ").upper()
    stock_list = [s.strip() for s in stocks.split(",") if s.strip()]

    if len(stock_list) < 2:
        print("❌ Error: Please enter at least two stock symbols.")
        return

    data = {}
    for stock in stock_list:
        try:
            stock_info = yf.Ticker(stock).info
            data[stock] = {
                'Stock Ticker': stock,
                'Company Name': stock_info.get('longName', 'N/A'),
                'Current Market Price': f"${stock_info.get('currentPrice', 'N/A'):,.2f}"
            }
        except Exception as e:
            print(f"❌ Error fetching data for {stock}: {e}")

    df_task1 = pd.DataFrame(data).T
    print("\n✅ Task 1 Output:\n")
    print(df_task1.to_string(index=False))

### ✅ Task 2.1: Fetch Stock Metrics (52-Week High, Low, ROA) ###
def fetch_stock_metrics():
    stocks = input("Enter stock symbols for Task 2.1: ").upper()
    stock_list = [s.strip() for s in stocks.split(",") if s.strip()]

    data = {}
    for stock in stock_list:
        try:
            stock_info = yf.Ticker(stock).info
            data[stock] = {
                'Stock Ticker': stock,
                'Company Name': stock_info.get('longName', 'N/A'),
                '52-Week High': f"${stock_info.get('fiftyTwoWeekHigh', 'N/A'):,.2f}",
                '52-Week Low': f"${stock_info.get('fiftyTwoWeekLow', 'N/A'):,.2f}",
                'ROA (%)': f"{stock_info.get('returnOnAssets', 'N/A') * 100:.2f}%" if stock_info.get('returnOnAssets') else "N/A"
            }
        except Exception as e:
            print(f"❌ Error fetching data for {stock}: {e}")

    df_task2 = pd.DataFrame(data).T
    print("\n✅ Task 2.1 Output:\n")
    print(df_task2.to_string(index=False))

### ✅ Task 2.2: Fetch Trending Stocks ###
def fetch_trending_stocks():
    trending_tickers = ["AAPL", "MSFT", "NVDA", "TSLA", "AMZN"]

    data = {}
    for stock in trending_tickers:
        try:
            stock_info = yf.Ticker(stock).info
            data[stock] = {
                'Stock Ticker': stock,
                'Company Name': stock_info.get('longName', 'N/A'),
                'Current Price': f"${stock_info.get('currentPrice', 'N/A'):,.2f}",
                '52-Week High': f"${stock_info.get('fiftyTwoWeekHigh', 'N/A'):,.2f}",
                '52-Week Low': f"${stock_info.get('fiftyTwoWeekLow', 'N/A'):,.2f}"
            }
        except Exception as e:
            print(f"❌ Error fetching data for {stock}: {e}")

    df_trending = pd.DataFrame(data).T
    print("\n✅ Task 2.2 Output: Trending Stocks\n")
    print(df_trending.to_string(index=False))

### ✅ Bonus Task: Fetch Elon Musk's Stocks ###
def fetch_elon_musk_stocks():
    elon_musk_stocks = ["TSLA", "GOOGL"]  # SpaceX, Neuralink, and Boring Co are private

    data = {}
    for stock in elon_musk_stocks:
        try:
            stock_info = yf.Ticker(stock).info
            data[stock] = {
                'Stock Ticker': stock,
                'Company Name': stock_info.get('longName', 'N/A'),
                'Current Price': f"${stock_info.get('currentPrice', 'N/A'):,.2f}",
                '52-Week High': f"${stock_info.get('fiftyTwoWeekHigh', 'N/A'):,.2f}",
                '52-Week Low': f"${stock_info.get('fiftyTwoWeekLow', 'N/A'):,.2f}"
            }
        except Exception as e:
            print(f"❌ Error fetching data for {stock}: {e}")

    df_elon = pd.DataFrame(data).T
    print("\n✅ Bonus: Elon Musk's Stocks\n")
    print(df_elon.to_string(index=False))

### 🔹 RUN TASKS ###
fetch_stock_data()  # Task 1
fetch_stock_metrics()  # Task 2.1
fetch_trending_stocks()  # Task 2.2
fetch_elon_musk_stocks()  # Bonus Task

