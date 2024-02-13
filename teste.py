import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from numpy.random import randint
from random import choice
from random import uniform

class StructuredDataPreprocessing():
    def __init__(self, X, y) -> None:
        self.X = X
        self.y = y
        self.numerical_features = list(X.select_dtypes(include=[np.int64, np.float64]).columns)
        self.categorical_features = list(X.select_dtypes(include=[np.object_]).columns)

    def featuresEncoder(self) -> pd.DataFrame:
        le = LabelEncoder()

        for name_column in self.numerical_features:
            self.X[name_column] = self.X[name_column].astype(float)

        for name_column in self.categorical_features:
            self.X[name_column] = le.fit_transform(self.X[name_column])
            if len(self.X[name_column].unique()) >= self.X.shape(0) / (3/2):
                self.X = self.X.drop(columns =[name_column])

        pd.DataFrame(self.X).to_numpy()

        return self.X
    
    def labelEncoder(self) -> pd.DataFrame:
        #

