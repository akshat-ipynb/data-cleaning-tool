import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, data):
        self.data = data

    def remove_duplicates(self):
        self.data = self.data.drop_duplicates()

    def remove_null_values(self, threshold=0.5):
        self.data = self.data.dropna(thresh=threshold * len(self.data), axis=1)

    def fill_missing_values(self, fill_value):
        self.data = self.data.fillna(fill_value)

    def remove_outliers(self, column, z_threshold=3):
        z_scores = np.abs((self.data[column] - self.data[column].mean()) / self.data[column].std())
        self.data = self.data[z_scores < z_threshold]

    def convert_to_numeric(self, column):
        self.data[column] = pd.to_numeric(self.data[column], errors='coerce')

    def standardize_column_names(self):
        self.data.columns = self.data.columns.str.strip().str.lower().str.replace(' ', '_')

    def remove_special_characters(self, column):
        self.data[column] = self.data[column].str.replace('[^a-zA-Z0-9\s]', '', regex=True)

    def run_all_cleaning(self):
        self.remove_duplicates()
        self.remove_null_values()