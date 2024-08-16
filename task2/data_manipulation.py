import pandas as pd

df = pd.read_csv('../data/cleaned_airbnb_data.csv')

print(df.iloc[0:5, 0:3])
print(df.loc[0:4, ['name', 'price', 'neighbourhood_group']])

# Filter the dataset for specific neighborhoods
manhattan_brooklyn = df[df['neighbourhood_group'].isin(['Manhattan', 'Brooklyn'])]

# Filter for price > $100 and number_of_reviews > 10
filtered_df = manhattan_brooklyn[(manhattan_brooklyn['price'] > 100) &
                                 (manhattan_brooklyn['number_of_reviews'] > 10)]

# Select columns of interest
columns_of_interest = ['neighbourhood_group', 'price', 'minimum_nights',
                       'number_of_reviews', 'price_category', 'availability_365']
selected_df = filtered_df[columns_of_interest]

# Group by neighbourhood_group and price_category
grouped = selected_df.groupby(['neighbourhood_group', 'price_category'])

# Calculate aggregate statistics
agg_stats = grouped.agg({
    'price': 'mean',
    'minimum_nights': 'mean',
    'number_of_reviews': 'mean',
    'availability_365': 'mean'
})

print(agg_stats)

# Sort by price (descending) and number_of_reviews (ascending)
sorted_df = selected_df.sort_values(['price', 'number_of_reviews'],
                                    ascending=[False, True])

# Ranking neighborhoods based on total listings and average price
neighborhood_rankings = df.groupby('neighbourhood_group').agg({
    'id': 'count',
    'price': 'mean'
}).sort_values(['id', 'price'], ascending=[False, False])

neighborhood_rankings.columns = ['total_listings', 'average_price']
print(neighborhood_rankings)


def print_grouped_data(grouped_df, message=None):
    if message:
        print(message)
    print(grouped_df)
    print("\nDataFrame Info:")
    print(grouped_df.info())


print_grouped_data(agg_stats, "Aggregated Statistics by Neighborhood and Price Category:")
print_grouped_data(neighborhood_rankings, "Neighborhood Rankings:")

agg_stats.to_csv('../data/aggregated_data.csv')

print("Filtered DataFrame shape:", filtered_df.shape)
print("\nAggregated Statistics shape:", agg_stats.shape)
print("\nNeighborhood Rankings shape:", neighborhood_rankings.shape)
