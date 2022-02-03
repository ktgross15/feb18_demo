# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
transactions_unknown_scored = dataiku.Dataset("transactions_unknown_scored")
df = transactions_unknown_scored.get_dataframe(limit=1000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['new_col'] = 'hello!'

# hello everyone!

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
transactions_python = dataiku.Dataset("transactions_python")
transactions_python.write_with_schema(df)