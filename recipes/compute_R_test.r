library(dataiku)

# Recipe inputs
transactions_stacked <- dkuReadDataset("transactions_stacked", samplingMethod="head", nbRows=100000, inferColClassesFromData = FALSE)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
R_test <- transactions_stacked # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(R_test,"R_test")
