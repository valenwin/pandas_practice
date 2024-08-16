import unittest
import pandas as pd

from io import StringIO
import sys

from task3.advanced_data_manipulation import (
    classify_availability,
    print_analysis_results
)


class TestAdvancedAnalysis(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'id': range(1, 6),
            'neighbourhood_group': ['Manhattan', 'Brooklyn', 'Queens', 'Manhattan', 'Brooklyn'],
            'room_type': ['Entire home/apt', 'Private room', 'Shared room', 'Entire home/apt', 'Private room'],
            'price': [100, 50, 30, 150, 80],
            'minimum_nights': [1, 2, 1, 3, 2],
            'number_of_reviews': [10, 5, 2, 15, 8],
            'availability_365': [30, 60, 90, 120, 180],
            'last_review': pd.date_range(start='2023-01-01', periods=5)
        })

    def test_pricing_pivot(self):
        pricing_pivot = pd.pivot_table(self.df, values='price', index='neighbourhood_group',
                                       columns='room_type', aggfunc='mean')
        self.assertIsInstance(pricing_pivot, pd.DataFrame)
        self.assertEqual(pricing_pivot.index.name, 'neighbourhood_group')
        self.assertEqual(pricing_pivot.columns.name, 'room_type')

    def test_long_format_transformation(self):
        df_long = pd.melt(self.df, id_vars=['id', 'neighbourhood_group', 'room_type'],
                          value_vars=['price', 'minimum_nights'],
                          var_name='metric', value_name='value')
        self.assertIsInstance(df_long, pd.DataFrame)
        self.assertIn('metric', df_long.columns)
        self.assertIn('value', df_long.columns)

    def test_classify_availability(self):
        self.assertEqual(classify_availability(30), "Rarely Available")
        self.assertEqual(classify_availability(100), "Occasionally Available")
        self.assertEqual(classify_availability(250), "Highly Available")

    def test_availability_analysis(self):
        self.df['availability_status'] = self.df['availability_365'].apply(classify_availability)
        availability_analysis = self.df.groupby('availability_status').agg({
            'price': 'mean',
            'number_of_reviews': 'mean',
            'neighbourhood_group': lambda x: x.value_counts().index[0]
        })
        self.assertIsInstance(availability_analysis, pd.DataFrame)
        self.assertIn('price', availability_analysis.columns)
        self.assertIn('number_of_reviews', availability_analysis.columns)
        self.assertIn('neighbourhood_group', availability_analysis.columns)

    def test_descriptive_statistics(self):
        numeric_columns = ['price', 'minimum_nights', 'number_of_reviews', 'availability_365']
        desc_stats = self.df[numeric_columns].describe()
        self.assertIsInstance(desc_stats, pd.DataFrame)
        self.assertEqual(len(desc_stats.columns), len(numeric_columns))

    def test_time_series_analysis(self):
        self.df['last_review'] = pd.to_datetime(self.df['last_review'])
        self.df.set_index('last_review', inplace=True)
        monthly_reviews = self.df.resample('M')['number_of_reviews'].sum()
        monthly_prices = self.df.resample('M')['price'].mean()
        self.assertIsInstance(monthly_reviews, pd.Series)
        self.assertIsInstance(monthly_prices, pd.Series)

    def test_seasonal_analysis(self):
        self.df['last_review'] = pd.to_datetime(self.df['last_review'])
        self.df.set_index('last_review', inplace=True)
        seasonal_analysis = self.df.groupby(self.df.index.month).agg({
            'price': 'mean',
            'number_of_reviews': 'mean'
        })
        self.assertIsInstance(seasonal_analysis, pd.DataFrame)
        self.assertEqual(len(seasonal_analysis), 1)

    def test_print_analysis_results(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        df_result = self.df.head()
        print_analysis_results(df_result, "Test DataFrame")

        series_result = self.df['price']
        print_analysis_results(series_result, "Test Series")

        other_result = "Test String"
        print_analysis_results(other_result, "Test Other")

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Test DataFrame", output)
        self.assertIn("Test Series", output)
        self.assertIn("Test Other", output)


if __name__ == '__main__':
    unittest.main()
