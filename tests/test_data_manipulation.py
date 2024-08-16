import unittest
import pandas as pd
from pandas.testing import assert_frame_equal


class TestDataManipulation(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv('../data/cleaned_airbnb_data.csv')

    def test_initial_dataframe_shape(self):
        expected_shape = (self.df.shape[0], 18)
        self.assertEqual(self.df.shape, expected_shape)

    def test_filter_manhattan_brooklyn(self):
        manhattan_brooklyn = self.df[self.df['neighbourhood_group'].isin(['Manhattan', 'Brooklyn'])]
        self.assertTrue(all(manhattan_brooklyn['neighbourhood_group'].isin(['Manhattan', 'Brooklyn'])))

    def test_filtered_df(self):
        manhattan_brooklyn = self.df[self.df['neighbourhood_group'].isin(['Manhattan', 'Brooklyn'])]
        filtered_df = manhattan_brooklyn[(manhattan_brooklyn['price'] > 100) &
                                         (manhattan_brooklyn['number_of_reviews'] > 10)]
        self.assertTrue(all(filtered_df['price'] > 100))
        self.assertTrue(all(filtered_df['number_of_reviews'] > 10))

    def test_selected_columns(self):
        manhattan_brooklyn = self.df[self.df['neighbourhood_group'].isin(['Manhattan', 'Brooklyn'])]
        filtered_df = manhattan_brooklyn[(manhattan_brooklyn['price'] > 100) &
                                         (manhattan_brooklyn['number_of_reviews'] > 10)]
        columns_of_interest = ['neighbourhood_group', 'price', 'minimum_nights',
                               'number_of_reviews', 'price_category', 'availability_365']
        selected_df = filtered_df[columns_of_interest]
        self.assertEqual(list(selected_df.columns), columns_of_interest)

    def test_neighborhood_rankings(self):
        neighborhood_rankings = self.df.groupby('neighbourhood_group').agg({
            'id': 'count',
            'price': 'mean'
        }).sort_values(['id', 'price'], ascending=[False, False])

        neighborhood_rankings.columns = ['total_listings', 'average_price']

        expected_rankings = pd.DataFrame({
            'total_listings': [21660, 20095],
            'average_price': [196.884, 124.438]
        }, index=['Manhattan', 'Brooklyn'])

        expected_rankings.columns = ['total_listings', 'average_price']

        neighborhood_rankings.index.name = None

        assert_frame_equal(neighborhood_rankings.loc[['Manhattan', 'Brooklyn']], expected_rankings)


if __name__ == '__main__':
    unittest.main()
