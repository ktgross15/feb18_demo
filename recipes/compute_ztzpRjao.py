# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
transactions_known = dataiku.Dataset("transactions_known")
df = transactions_known.get_dataframe(limit=10000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
model = RandomForestClassifier()
model.fit(X, y)

today = datetime.date.today()
filename = 'model_{}-{}-{}.pkl'.format(today.year, today.month, today.day)

model_folder = dataiku.Folder("model_folder")
with model_folder.get_writer(filename) as w:
    pickle.dump(model, w)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
model_folder = dataiku.Folder("ztzpRjao")
model_folder_info = model_folder.get_info()