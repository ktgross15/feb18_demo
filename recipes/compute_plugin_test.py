# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
cardholder_info_copy = dataiku.Dataset("cardholder_info_copy")
cardholder_info_copy_df = cardholder_info_copy.get_dataframe()




# Write recipe outputs
plugin_test = dataiku.Dataset("plugin_test")
plugin_test.write_with_schema(plugin_test_df)
