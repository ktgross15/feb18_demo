# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
transactions_known = dataiku.Dataset("transactions_known")
transactions_known_df = transactions_known.get_dataframe()




# Write recipe outputs
model_folder = dataiku.Folder("ztzpRjao")
model_folder_info = model_folder.get_info()
