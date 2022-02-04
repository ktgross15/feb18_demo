# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd
import numpy as np
import datetime
import pickle
from sklearn.ensemble import RandomForestClassifier

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
transactions_known = dataiku.Dataset("transactions_known")
df = transactions_known.get_dataframe(limit=10000)

#yooooo

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.dropna(inplace=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# features = ['purchase_month','purchase_dow','purchase_hour','merchant_category_id','purchase_amount','days_active',
#             'card_fico_score','card_age','merchant_cardholder_distance']

features = ['merchant_category_id','purchase_amount','days_active','card_fico_score','card_age','merchant_cardholder_distance']

target = 'authorized_flag'

X = df[features].values
y = df[target]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
model = RandomForestClassifier()
model.fit(X, y)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# today = datetime.date.today()
# filename = 'model_{}-{}-{}.pkl'.format(today.year, today.month, today.day)
filename = 'model.pkl'

model_folder = dataiku.Folder("model_folder")
with model_folder.get_writer(filename) as w:
    pickle.dump(model, w)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
# model_folder = dataiku.Folder("ztzpRjao")
# model_folder_info = model_folder.get_info()