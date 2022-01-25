# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
transactions_unknown_scored = dataiku.Dataset("transactions_unknown_scored")
transactions_unknown_scored_df = transactions_unknown_scored.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

transactions_python_df = transactions_unknown_scored_df # For this sample code, simply copy input to output


# Write recipe outputs
transactions_python = dataiku.Dataset("transactions_python")
transactions_python.write_with_schema(transactions_python_df)
