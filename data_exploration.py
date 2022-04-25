# Library imports for data exploration
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file, by path, into a pandas DataFrame object
file_path = "C:/Users/TawfikAbbas/Documents/TalentPath/CapstoneProject/data/merged_data_cleaned.csv"

df = pd.read_csv(file_path)

# Basic summary info about the dataset
df.info()

# Separate the outputs in the terminal 
print("\n")

# Output the shape of the DataFrame
print("Dimensions of the DataFrame:", df.shape, "\n")

# Identify columns with missing values
print("Columns with missing values: \n", df.isnull().sum(), "\n")

# Identify columns missing more than 20% of the possible total (1339)
bucket = [col for col in df.columns if df[col].isnull().sum() > np.floor(0.20 * df.shape[0])]

print("Columns missing more than 20 percent of rows: \n", bucket)