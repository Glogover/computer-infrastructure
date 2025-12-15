# Computer Infrastructure

This repository contains coursework for the **Computer Infrastructure** module at **Atlantic Technological University (ATU)**.  
It focuses on using Python to work with system tools, data analysis libraries, external APIs, and basic automation.

The repository demonstrates:
- Downloading financial data programmatically
- Storing data in a structured way
- Visualising data
- Working with Python scripts and Jupyter notebooks

---

## Repository Contents

### `faang.py`
A standalone Python script that works with real-world financial data.

When run from the command line, the script:
1. Downloads recent **hourly stock price data** for the FAANG companies:
   - META
   - AAPL
   - AMZN
   - NFLX
   - GOOG
2. Saves the data as a **timestamped CSV file** in a `data/` directory
3. Loads the most recent CSV file
4. Generates and saves a **plot of closing prices** in a `plots/` directory

The script uses:
- `yfinance` for data retrieval
- `pandas` for data handling
- `matplotlib` for plotting
- `pathlib` for filesystem management

---

### `problems.ipynb`
A Jupyter Notebook containing a series of **practical problems** related to:

- Downloading financial data with `yfinance`
- Working with time-series data
- Saving and loading CSV files
- Data inspection and analysis using `pandas`
- Plotting and visualisation

This notebook is intended to be run interactively and documents the steps taken to solve each problem.

---

## Requirements

You will need **Python 3** installed.

Required Python packages:
- pandas
- yfinance
- matplotlib
- jupyter (for the notebook)

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/computer-infrastructure.git
   cd computer-infrastructure

2. **Install dependencies**
   ```bash
   pip install pandas yfinance matplotlib jupyter

--- 

## How to Run the Code

1. **Running the Jupyter Notebook**
   ```bash
   jupyter notebook
   problems.ipynb

2. **Running the Python Script**
   ```bash
   ./faang.py

--- 

**Author:**
*Marcin Kaminski*




