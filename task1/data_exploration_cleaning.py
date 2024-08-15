import pandas as pd

# Load the dataset
df = pd.read_csv('../data/AB_NYC_2019.csv')

# Inspect the first few rows
print(df.head())

# Get basic information about the dataset
print(df.info())

# Identify columns with missing values
print(df.isnull().sum())

# Handle missing values
df['name'].fillna('Unknown', inplace=True)
df['host_name'].fillna('Unknown', inplace=True)
df['last_review'].fillna(pd.NaT, inplace=True)


# Categorize listings by price range
def price_category(price):
    if price < 100:
        return 'Low'
    elif 100 <= price < 300:
        return 'Medium'
    else:
        return 'High'


df['price_category'] = df['price'].apply(price_category)


# Categorize listings by length of stay
def length_of_stay_category(nights):
    if nights <= 3:
        return 'short-term'
    elif 4 <= nights <= 14:
        return 'medium-term'
    else:
        return 'long-term'


df['length_of_stay_category'] = df['minimum_nights'].apply(length_of_stay_category)

# Verify no missing values in critical columns
print(df[['name', 'host_name', 'last_review']].isnull().sum())

# Remove rows with price equal to 0
df = df[df['price'] > 0]


def print_dataframe_info(dataframe, message=None):
    if message:
        print(message)
    print(f"Number of entries: {len(dataframe)}")
    print("\nMissing values:")
    print(dataframe.isnull().sum())
    print("\nDataFrame Info:")
    dataframe.info()


if __name__ == "__main__":
    print_dataframe_info(df, "Before cleaning:")
    print_dataframe_info(df, "After cleaning:")
    df.to_csv('../data/cleaned_airbnb_data.csv', index=False)
