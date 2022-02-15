library(dataiku)

# Recipe inputs
transactions_stacked_prepared <- dkuReadDataset("transactions_stacked_prepared", samplingMethod="head", nbRows=100000, 
                                                inferColClassesFromData = FALSE)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
transactions_R <- transactions_stacked_prepared # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(transactions_R,"transactions_R")
