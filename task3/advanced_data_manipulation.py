import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('../data/cleaned_airbnb_data.csv')

# Analyze Pricing Trends Across Neighborhoods and Room Types
pricing_pivot = pd.pivot_table(df, values='price', index='neighbourhood_group',
                               columns='room_type', aggfunc='mean')
print("Average Price by Neighborhood and Room Type:")
print(pricing_pivot)

# Transform dataset from wide to long format
df_long = pd.melt(df, id_vars=['id', 'neighbourhood_group', 'room_type'],
                  value_vars=['price', 'minimum_nights'],
                  var_name='metric', value_name='value')
print("\nLong Format Sample:")
print(df_long.head())


# Classify Listings by Availability
def classify_availability(days):
    if days < 50:
        return "Rarely Available"
    elif 50 <= days <= 200:
        return "Occasionally Available"
    else:
        return "Highly Available"


df['availability_status'] = df['availability_365'].apply(classify_availability)

# Analyze trends with the new availability_status
availability_analysis = df.groupby('availability_status').agg({
    'price': 'mean',
    'number_of_reviews': 'mean',
    'neighbourhood_group': lambda x: x.value_counts().index[0]
})
print("\nAvailability Status Analysis:")
print(availability_analysis)

# Perform basic descriptive statistics
numeric_columns = ['price', 'minimum_nights', 'number_of_reviews', 'availability_365']
desc_stats = df[numeric_columns].describe()
print("\nDescriptive Statistics:")
print(desc_stats)

# Convert last_review to datetime and set as index
df['last_review'] = pd.to_datetime(df['last_review'])
df.set_index('last_review', inplace=True)

# Resample data to observe monthly trends
monthly_reviews = df.resample('M')['number_of_reviews'].sum()
monthly_prices = df.resample('M')['price'].mean()

print("\nMonthly Review Trends:")
print(monthly_reviews.head())
print("\nMonthly Price Trends:")
print(monthly_prices.head())

# Analyze seasonal patterns
seasonal_analysis = df.groupby(df.index.month).agg({
    'price': 'mean',
    'number_of_reviews': 'mean'
})
seasonal_analysis.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print("\nSeasonal Analysis:")
print(seasonal_analysis)


def print_analysis_results(data, message=None):
    if message:
        print(message)
    if isinstance(data, pd.DataFrame):
        print(data)
        print("\nDataFrame Info:")
        print(data.info())
    elif isinstance(data, pd.Series):
        print(data)
        print("\nSeries Info:")
        print(data.describe())
    else:
        print(data)


# Use the function to display results
print_analysis_results(pricing_pivot, "Pricing Trends Across Neighborhoods and Room Types:")
print_analysis_results(availability_analysis, "Availability Status Analysis:")
print_analysis_results(desc_stats, "Descriptive Statistics:")
print_analysis_results(seasonal_analysis, "Seasonal Analysis:")

# Save the time series data
time_series_data = pd.concat([monthly_reviews, monthly_prices], axis=1)
time_series_data.columns = ['monthly_reviews', 'monthly_prices']
time_series_data.to_csv('../data/time_series_data.csv')

# Verify the results
print("\nTime Series Data Sample:")
print(time_series_data.head())
print("\nTime Series Data Info:")
print(time_series_data.info())
