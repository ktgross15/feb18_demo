from  dataiku.apinode.predict.predictor import ClassificationPredictor
import pandas as pd
import pickle
import os

class MyPredictor(ClassificationPredictor):

    def __init__(self, data_folder = None):
        self.data_folder = data_folder
        model_file = os.path.join(self.data_folder,'model.pkl')
        self.model = pickle.load(open(model_file,'r'))

    def predict(self, features_df):
        model = self.model
        predictions = model.predict(features_df)
        return predictions
