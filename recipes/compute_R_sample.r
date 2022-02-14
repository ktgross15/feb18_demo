library(dataiku)

# Recipe inputs
transactions_known <- dkuReadDataset("transactions_known", samplingMethod="head", nbRows=10000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
R_sample <- transactions_known # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(R_sample,"R_sample")
