# Output a summary of each variable to a single text file
# Save a histogram of each variable to png files
# Output a scatter plot of each pair of variables

# Import Pandas Library
import pandas as pd 

# Load the iris.csv file into program
df = pd.read_csv('iris.csv')


# Open a file to write the summary 
with open("summary.txt", "w") as f:

