# Pandas Data Analysis Tasks

This project contains a series of Python scripts using Pandas for data analysis.
The project is divided into three main tasks, each focusing on different aspects of data manipulation and analysis using the New York City Airbnb Open Data.

## Project Structure
```
numpy_practice/
│
├── task1/
│   ├── __init__.py
│   ├── data_exploration_cleaning.py
│
├── task2/
│   ├── __init__.py
│   ├── data_manipulation.py
│
├── task3/
│   ├── __init__.py
│   ├── advanced_data_manipulation.py
│
├── tests/
│   ├── __init__.py
│   ├── test_advanced_data_manipulation.py
│   ├── test_data_exploration_cleaning.py
│   ├── test_data_manipulation.py
│
│
└── README.md
```

## Tasks Overview

### Task 1: Basic Data Exploration and Cleaning
- File: `data_exploration_cleaning.py`
- Test File: `test_data_exploration_cleaning.py`
- Description: Introduces basic data exploration and cleaning techniques using Pandas on the NYC Airbnb dataset.

### Task 2: Data Selection, Filtering, and Aggregation
- File: `data_manipulation.py`
- Test File: `test_data_manipulation.py`
- Description: Focuses on selecting, filtering, and aggregating data within the NYC Airbnb dataset using Pandas.

### Task 3: Advanced Data Manipulation, Descriptive Statistics, and Time Series Analysis
- File: `advanced_data_manipulation.py`
- Test File: `test_advanced_data_manipulation.py`
- Description: Covers advanced data manipulation, descriptive statistics, and time series analysis on the NYC Airbnb dataset using Pandas.

## Running the Scripts

To run each task's script: <br> 
`python task1/data_exploration_cleaning.py` <br> 
`python task2/data_manipulation.py` <br> 
`python task3/advanced_data_manipulation.py` <br> 

## Running the Tests

To run tests for a specific task: <br> 
`python -m unittest tests/test_data_exploration_cleaning.py` <br> 
`python -m unittest tests/test_data_manipulation.py` <br>
`python -m unittest tests/test_advanced_data_manipulation.py` <br>

To run all tests: <br> 
`python -m unittest tests` <br> 

## Requirements

- Python 3.x
- Pandas
- Matplotlib (for visualization, if included)

Install the required packages using:

`pip install -r requirements.txt`

## Data Source

The New York City Airbnb Open Data used in this project is available on Kaggle:
[New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
