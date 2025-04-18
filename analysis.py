# Output a summary of each variable to a single text file
# Save a histogram of each variable to png files
# Output a scatter plot of each pair of variables

# Import Pandas Library
import pandas as pd 

# Load the iris.csv file into program
data = pd.read_csv('iris.csv')

# Data set summary will focus on Values: Mean,Minimum,Maximum,Standard Deviation,Median

# Open a file to write the summary
with open("summary.txt", "w") as summary_file:
    
# Go through each numeric column in the dataset
# Select_dtypes() method in Pandas to select columns based on their data type 
# ref:https://www.w3schools.com/python/pandas/ref_df_select_dtypes.asp
    for column in data.select_dtypes(include='number').columns:

# Find the figures for each column and round to two decimal places
# Average value
        mean = round(data[column].mean(), 2) 
# Smallest value     
        min_val = round(data[column].min(), 2)
# Largest value    
        max_val = round(data[column].max(), 2) 
# Standard deviation   
        std_dev = round(data[column].std(), 2)  
# Median value  
        median = round(data[column].median(), 2)  
        

# Input the stats collected into the file 
        summary_file.write(f"{column}:\n")
        summary_file.write(f"  Mean: {mean}\n")
        summary_file.write(f"  Min: {min_val}\n")
        summary_file.write(f"  Max: {max_val}\n")
        summary_file.write(f"  Std Dev: {std_dev}\n")
        summary_file.write(f"  Median: {median}\n\n")

# Process text columns
# include=object makes sure to include non numeric types 
    for column in data.select_dtypes(include='object').columns:
        # Get summary statistics for text columns
        num_unique = data[column].nunique()
        most_common = data[column].mode()[0]
        count_most_common = data[column].value_counts().iloc[0]

        # Write stats for text columns to the file
        # F-string allows us to insert variable into the string (column)
        # \n Newline character is used to move to next line after  string
        summary_file.write(f"{column}:\n")
        summary_file.write(f"  Number of unique values: {num_unique}\n")
        summary_file.write(f"  Most common value: {most_common}\n")
        summary_file.write(f"  Occurrences of most common value: {count_most_common}\n\n")

# Print summary to summary.txt to display all information
print("Summary to summary.txt")