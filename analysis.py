# Output a summary of each variable to a single text file
# Save a histogram of each variable to png files
# Output a scatter plot of each pair of variables

# Import All Relevant Libraries
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

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

# 2. Save a histogram of each variable to png files

# Load the Dataset
iris = load_iris()
# Extract the feature data
data = iris.data 
# Get lost of feature names
feature_names = iris.feature_names

# Loop each feature in the dataset to create histogram
for i in range(len(feature_names)):
    # Set figure size for a more clear histogram    
    plt.figure(figsize=(8, 5))
    # Set bins to 10 for and colours to green with edge colour black for a clean Histogram
    plt.hist(data[:, i], bins=10, color='green', edgecolor='black')
    # Set title for 'Histogram of feature name' 
    plt.title(f'Histogram of {feature_names[i]}')
    # Set x axis to include feature name
    plt.xlabel(feature_names[i])
    # Set y axis to show Frequency 
    plt.ylabel('Frequency')

# Create safe of feature name for use in a filename
# Use replace to change all spaces into underscores and remove gaps
    safe_name = feature_names[i].replace(" ", "_").replace("(", "").replace(")", "") 
    # Save the plot as png file    
    plt.savefig(f'{safe_name}_histogram.png') 
    # Print confirmation of saved file    
    print(safe_name + ' to '+ safe_name + '_histogram.png')
    # Clear current plot to prepare for next one
    plt.clf()
    
# 3. Output a scatter plot of each pair of variables. 

# Label each column using feature names
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# Store the list of feature names in a seperate variable 
features = iris.feature_names

# Loop all feature pairs without repetition
for i in range(len(features)):
        for j in range(i + 1, len(features)):

                # Set x and y axis labels using feature names
                x_label = features[i]
                y_label = features[j]

                # Create a new figure with specified width and height
                plt.figure(figsize=(6,4))

                # Create scatter plot with x and y axes
                # Colour set to green, edges black, alpha for transparency
                plt.scatter(df[x_label], df[y_label], color='green', edgecolor='black', alpha=0.8)
                # Label the x-axis
                plt.xlabel(x_label)
                # Label the y-axis
                plt.ylabel(y_label)
                # Set Title
                plt.title(f'{x_label} v {y_label}')
                # Plot Grid
                plt.grid(True)

                # Clean the feature names so no overlap between files
                safe_x = x_label.replace(" ", "_").replace("(", "").replace(")","")
                safe_y = y_label.replace(" ", "_").replace("(", "").replace(")","")
                # Save the scattter plot to png file 
                plt.savefig(f'{x_label}_vs_{y_label}.png')
                # Print confirmation message
                print(f"{safe_x} vs {safe_y}")
                # Clear current figure for no overlap
                plt.clf()

# 4. Perform any other analysis you think is appropriate
# For the last task I decided to perform a pairplot of the data set
# The pairplot creates a matrix of scatter plots showing every possible pair combination of features.
# I have color coded each point based on the flower class.
# This helps identify correlations and class separations visually.
# The diagonal of the pairplot where the x and y features are the same contains histograms.
# These histograms show the distribution of each feature.

# Check that a target column (e.g. 'species' or 'class') exists
df_csv = pd.read_csv('iris.csv')

# Load the target labels (0, 1, 2) and their names (setosa, versicolor, virginica)
iris = load_iris()
target_labels = iris.target
target_names = iris.target_names

# Map numerical values to species names
species = [target_names[i] for i in target_labels]

# If the length of data matches add species column
if len(df_csv) == len(species):
    df_csv['species'] = species

# Create seaborn pairplot
sns.pairplot(df_csv, hue='species', diag_kind='hist')
plt.savefig('seaborn_pairplot.png')
print("Seaborn pairplot saved as seaborn_pairplot.png")

