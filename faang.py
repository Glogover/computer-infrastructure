#!/usr/bin/env python3

"""
faang.py

Created by Marcin Kaminski as part of academic coursework for Computer Infrastructure
at the Atlantic Technological University (ATU).
"""

"""
When run from the terminal (./faang.py), this script:
1. Downloads recent FAANG stock data
2. Saves it as a timestamped CSV
3. Loads the most recent CSV
4. Creates and saves a plot of Close prices
"""

# Import required libraries.

# Dates and times.
import datetime as dt # For handling dates and times. 
# Sourced from: https://realpython.com/ref/stdlib/datetime/

# Data frames.
import pandas as pd # For data manipulation and analysis. 
# https://en.wikipedia.org/wiki/Pandas_(software)
# Sourced from: https://www.geeksforgeeks.org/python/how-to-install-python-pandas-on-windows-and-linux/

# Yahoo Finance data.
import yfinance as yf # For downloading financial data from Yahoo Finance. 
# https://en.wikipedia.org/wiki/Yahoo_Finance
# https://github.com/ranaroussi/yfinance
# Sourced from: https://www.geeksforgeeks.org/python/how-to-import-yfinance-as-yf-in-python/

# Plotting.
import matplotlib.pyplot as plt # For creating static, animated, and interactive visualizations.
# Sourced from: https://matplotlib.org/2.0.2/users/pyplot_tutorial.html

# File system paths.
from pathlib import Path # For handling filesystem paths in an object-oriented way.
# Sourced from: https://docs.python.org/3/library/pathlib.html


def get_data(days=5, interval='1h', folder='./data/'): 
    """
    This function downloads FAANG stock data and saves it to a CSV file with the following default parameters:
    - days: 5 (downloads data for the last 5 days)
    - interval: '1h' (hourly data)
    - folder: './data/' (saves the file in the 'data' folder in the root directory)
    The filename format is "YYYYMMDD-HHmmss.csv".
    """

    # Define the list of FAANG stocks.
    FAANG = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    
    # Get the current date and time .
    now = dt.datetime.now()
    
    # Download hourly data for each FAANG stock.
    df = yf.download(FAANG, period=f'{days}d', interval=interval, auto_adjust=True)
    
    # Generate the filename with the current date and time.
    filename = folder + now.strftime("%Y%m%d-%H%M%S") + ".csv"
    
    # Save the data to a CSV file.
    df.to_csv(filename)

    return filename


def plot_data(data_folder='./data/', plots_folder='./plots/'):
    """
    Load the most recent CSV from data_folder, plot Close prices for FAANG,
    show the plot in the notebook, and save it into plots_folder.
    """
    # Define FAANG tickers.
    tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

    # Ensure folders exist.
    data_folder = Path(data_folder) # Convert to Path object.
    plots_folder = Path(plots_folder) # Convert to Path object.
    plots_folder.mkdir(parents=True, exist_ok=True) # Create plots folder if it doesn't exist.

    # Find latest CSV
    csv_files = sorted(data_folder.glob("*.csv"), key=lambda f: f.stat().st_mtime) # Sort by modification time.
    if not csv_files: # 
        raise FileNotFoundError("No CSV files found in the data folder.") # Raise error if no files found.
    latest_file = csv_files[-1] # Get the most recent file.

    # Load yfinance multi-index CSV
    df = pd.read_csv(latest_file, header=[0,1], index_col=0, parse_dates=True) # Read CSV with multi-index columns.

    # Extract Close prices for available tickers
    available = [t for t in tickers if t in df['Close'].columns] # Check available tickers.
    close_df = df['Close'][available] # Get Close prices.

    # Ensure we have rows
    close_df = close_df.dropna(how='all') # Drop rows where all values are NaN.
    if close_df.shape[0] == 0: # Check if any data is left.
        raise ValueError( # Raise error if no data available.
            "No usable price data found. "
            "Re-run get_data() with more days (e.g., days=10)."
        )

    # --- Create plot ---
    plt.figure(figsize=(12, 6)) # Set figure size.
    for t in available: # Loop through available tickers.
        plt.plot(close_df.index, close_df[t], label=t) # Plot each ticker's Close price.

    plt.xlabel("Time") # Set x-axis label.  
    plt.ylabel("Close Price (USD)") # Set y-axis label.
    plt.legend() # Show legend.

    title_date = pd.to_datetime(close_df.index[-1]).strftime("%Y-%m-%d %H:%M:%S") # Format title date.
    plt.title(f"FAANG Close Prices — {title_date}") # Set plot title.

    # --- Save plot ---
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S") # Current timestamp for filename.
    plot_path = plots_folder / f"{timestamp}.png" # Define plot file path.
    plt.savefig(plot_path, dpi=200, bbox_inches='tight') # Save plot to file.

    # --- Show plot in notebook ---
    plt.show() # Display the plot.

    # Close figure to free memory
    plt.close() # Close the plot.

    return str(plot_path) # Return the path to the saved plot.


def main(): 
    """
    Main function to get data and plot it.
    """
    csv_file = get_data() # Download and save FAANG stock data.
    plot = plot_data() # Load the latest data and create a plot.

    print(f"Data saved to: {csv_file}") # Print the path to the saved CSV file.
    print(f"Plot saved to: {plot}") # Print the path to the saved plot

if __name__ == "__main__":
    main() # Run the main function when the script is executed directly.


# End

