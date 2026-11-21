import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date
import sys

sys.path.append('..')

from utils import load_to_df

st.set_page_config(page_title="Stock Dashboard", layout="wide")

# ticker = yf.Ticker("AAPL")

# ticker.info.get('longName')
# ticker.info.get('sector')
# ticker.info.get('marketCap')

# ticker_list = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AIG', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'AXP', 
#               'BA', 'BAC', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK-B',
#               'C', 'CAT', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX', 
#               'DE', 'DHR', 'DIS', 'DUK', 'EMR', 'FDX', 'GD', 'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS',
#               'HD', 'HON', 'IBM', 'INTC', 'INTU', 'ISRG', 'JNJ', 'JPM', 'KO', 
#               'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MDT', 'MET', 'META', 'MMM', 'MO', 'MRK', 'MS', 'MSFT',
#               'NEE', 'NFLX', 'NKE', 'NOW', 'NVDA', 'ORCL', 'PEP', 'PFE', 'PG', 'PLTR', 'PM', 'PYPL', 
#               'QCOM', 'RTX', 'SBUX', 'SCHW', 'SO', 'SPG', 'T', 'TGT', 'TMO', 'TMUS', 'TSLA', 'TXN',
#               'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WFC', 'WMT', 'XOM']


# name_list = []
# sector_list = []
# market_cap_list = []
 
# for ticker in ticker_list:
#    stock = yf.Ticker(ticker)
#    info = stock.info

#    name_list.append(info.get('longName'))
#    sector_list.append(info.get('sector'))
#    market_cap = info.get('marketCap')
#    market_cap_bn = round(market_cap / 1e9, 2)
#    market_cap_list.append(market_cap_bn)

# ticker_info_df = pd.DataFrame({'Ticker': ticker_list, 'Company':name_list, 'Sector':sector_list, 'Market Cap (B)': market_cap_list})
# ticker_info_df.to_csv('ticker_info.csv', index=False)   


###

##ticker_info = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv")
# ticker_list = list(ticker_info.Ticker.unique())

# Download stock data
# start_date="2020-01-01"
# end_date = f"{date.today().year}-12-31"  

#stock_data = yf.download(ticker_list, start=start_date, end=end_date).stack(level='Ticker') \
#               .reset_index().rename(columns={'level_1': 'Ticker'})

# Save to CSV (index=False prevents pandas from saving the row numbers)
# stock_data.to_csv("stock_data_yf.csv", index=False)
# print("Data saved successfully!")
###

st.markdown("## 🎯 Task 1: Build a stock dashboard with sidebar controls")

st.markdown("### :material/dataset: Data & variables to use")


code = """
ticker_info = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv")

# extract S&P 100 tickers from ticker_info
ticker_list = list(ticker_info.Ticker.unique())

# Load the stock data
stock_data = pd.read_csv(
    "https://github.com/justinjiajia/datafiles/raw/refs/heads/main/stock_data_yf.csv", 
    parse_dates=['Date']
)
"""

st.code(code)
    



url = "https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv"

ticker_info = load_to_df(url)
st.write(ticker_info)

 
@st.cache_data(show_spinner=False)
def yf_download(symbol_list, start_date="2020-01-01", end_date=f"{date.today().year}-12-31"):
    # This transformation converts stock data from a wide format (where each ticker is a column) into a long format 
    # (where each ticker's data is in separate rows).
    return yf.download(symbol_list, start=start_date, end=end_date).stack(level='Ticker').reset_index().rename(columns={'level_1': 'Ticker'})


ticker_list = list(ticker_info.Ticker.unique())


stock_data = yf_download(ticker_list)

st.write(stock_data)



"---"

 
st.markdown("""### :material/description: Requirements

- Include a sidebar containing the following widgets:

    - A **checkbox** (`st.checkbox()`) to toggle the visibility of a bar chart visualizing the market caps of S&P 100 stocks by sector. This checkbox should be checked by default.
            
    - A **multiselect** (`st.multiselect()`) for users to choose which stocks from `ticker_list` to include in the plot. The default selections are `'TSLA'`, `'NVDA'`, and `'AAPL'`.
        - If no stocks are selected, display the error message `"Please select at least one stock!"` using `st.error()`.
        - If stocks are selected, display a line chart of their closing prices (column `'Close'`) and a bar chart of their volumes (column `'Volume'`).
     
    - A **slider** (`st.slider()`) for users to select the year range for stock comparison, ranging from 2020 to 2025. The default range is 2024 to 2025.

#### Tips

- Use [`DataFrame.query()`](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) to filter data for plotting. For example, if `selected_tickers` holds the chosen stocks and `selected_years` holds the year range, use `.query(f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' and Ticker in {selected_tickers}")` to get the filtered data.
""")


st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

# set page title
st.title("S&P 100 Stock Dashboard 📊")  



# Sidebar controls
with st.sidebar:

    show_sector = st.checkbox("Show Market Cap by Sector", True)

    selected_tickers = st.multiselect(
        "Select Companies",
        options=ticker_list,
        default=['TSLA', 'NVDA', 'AAPL']
    )

    # Year range slider
    selected_years = st.slider(
        "Select Year Range",
        min_value=2020,
        max_value=2025,
        value=(2024, 2025)
    )

if show_sector:
    st.header("Market Cap by Sector")
    st.bar_chart(ticker_info, x="Sector", y="Market Cap (B)", color="Ticker", horizontal=True,
            width=720, height=500)

if selected_tickers:

    chart_data = stock_data.query(f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' and Ticker in {selected_tickers}")


    st.header(f"Stock Trend Analysis ({selected_years[0]} - {selected_years[1]})")
    
    # Closing Prices
    st.subheader("Closing Prices")
    st.line_chart(chart_data, x="Date", y="Close", color="Ticker",
                  width=720, height=500)

    
    # Volume Analysis
    st.subheader("Trading Volume")
    st.bar_chart(chart_data, x="Date", y="Volume", color="Ticker", 
                  width=720, height=500)

else:
    st.error("Please select at least one stock") # st.warning("Please select at least one stock!")



"---"

st.markdown("""## 🎯 Task 2: Display a video based on user input
            
### :material/description:  Requirements

- Create a text input widget that allows the user to enter a video URL, e.g., `https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4`.
- Add a "Submit" button.
- Place the text input and the "Submit" button side-by-side on the same line. Use a wider column for the text input (e.g., a 2:1 ratio) and align the button to the bottom of the input box.
- When the button is clicked, display the video inside a bordered container below the input.
- If the URL is invalid or the video cannot be loaded, display an error message instead.
- Before submission, display an message "Please enter a video URL and click Submit to display the video." in the container.

#### Tips

- **Side-by-side Layout:** Use `st.columns()` to place elements horizontally. You can pass a list to specify the width ratio (e.g., `[2, 1]`) and set `vertical_alignment="bottom"` so the button lines up nicely with the text input.

- **State Management:** Because Streamlit reruns the script on every interaction, use `st.session_state` to store the submitted URL and a boolean flag (`clicked`) so the video stays visible even if the user types in the text box again.

- **Layout Containers:** Use `st.container()` to group the video display and apply layout options like `border=True`, `width=640`, `height=400`, and `horizontal_alignment="center"`.

- **Video Embedding:** `st.video()` accepts both direct video files (e.g., `.mp4`) and streaming platform links (like YouTube). 

- **Error handling:** Wrap `st.video()` in a `try...except` block to catch invalid URLs and display a custom [`st.error()`](https://docs.streamlit.io/develop/api-reference/status/st.error) instead of crashing the app.

""")



st.divider()


if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'url' not in st.session_state:
    st.session_state.url = ""

# 1. Render the input and button

col1, col2 = st.columns([2, 1], vertical_alignment="bottom")

url = col1.text_input("Enter the URL of a video", 
                    "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4",
                    key="_url")

button = col2.button('Submit')

if button:
    # Update state manually when clicked
    st.session_state.clicked = True
    st.session_state.url = url

video_container = st.container(border=True, width=640, height=400, horizontal_alignment="center")

if st.session_state.clicked:
    try:
        video_container.video(st.session_state.url, format="video/mp4", start_time=0, autoplay=True)
    except:
        video_container.error("Cannot find the video!")

else:
    video_container.info("Please enter a video URL and click Submit to display the video.")


"---"

st.markdown("### :material/widgets: :red[Starter code]")

starter_code = """

# 1. Initialize session state variables
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'url' not in st.session_state:
    st.session_state.url = ""

# 2. Render the input and button side-by-side
col1, col2 = ...

url = ...

button = ...

# 3. Handle button click
if button:
    st.session_state.clicked = ...
    st.session_state.url = ...

# 4. Create the container for the video display
video_container = ...

# 5. Display the video or the info message
if st.session_state.clicked:
   ...
else:
    video_container.info(...)


"""

st.code(starter_code)

