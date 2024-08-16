import unittest
import pandas as pd
from task1.data_exploration_cleaning import (
    price_category,
    length_of_stay_category,
)

data = {
    'name': ['Listing 1', None, 'Listing 3'],
    'host_name': ['Host 1', 'Host 2', None],
    'price': [150, 0, 350],
    'minimum_nights': [2, 5, 15],
    'last_review': ['2024-01-01', None, '2024-01-03']
}

df = pd.DataFrame(data)


class TestAirbnbDataProcessing(unittest.TestCase):

    def setUp(self):
        self.df = df.copy()

    def test_fill_missing_values(self):
        self.df['name'].fillna('Unknown', inplace=True)
        self.df['host_name'].fillna('Unknown', inplace=True)
        self.df['last_review'].fillna(pd.NaT, inplace=True)

        self.assertEqual(self.df['name'].isnull().sum(), 0)
        self.assertEqual(self.df['host_name'].isnull().sum(), 0)
        self.assertEqual(self.df['last_review'].isnull().sum(), 1)

    def test_price_category(self):
        self.df['price_category'] = self.df['price'].apply(price_category)
        expected_categories = ['Medium', 'Low', 'High']
        self.assertListEqual(list(self.df['price_category']), expected_categories)

    def test_length_of_stay_category(self):
        self.df['length_of_stay_category'] = self.df['minimum_nights'].apply(length_of_stay_category)
        expected_categories = ['short-term', 'medium-term', 'long-term']
        self.assertListEqual(list(self.df['length_of_stay_category']), expected_categories)

    def test_remove_zero_price(self):
        df_cleaned = self.df[self.df['price'] > 0]
        self.assertFalse((df_cleaned['price'] == 0).any())


if __name__ == "__main__":
    unittest.main()
