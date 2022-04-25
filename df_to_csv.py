# Library imports 
import numpy as np
import pandas as pd

# Read the CSV file, by path, into a pandas DataFrame object
file_path = "C:/Users/TawfikAbbas/Documents/TalentPath/CapstoneProject/data/merged_data_cleaned.csv"

df = pd.read_csv(file_path)

# Drop the column `Unnamed: 0` from the dataframe
df = df.drop(columns= 'Unnamed: 0')

# Rename columns with the character "." 
rename_dict = {
    "Country.of.Origin" : "country_of_origin",
    "Farm.Name" : "farm_name",
    "Lot.Number" : "lot_number",
    "ICO.Number" : "ICO_number",
    "Number.of.Bags" : "number_of_bags",
    "Bag.Weight" : "bag_weight",
    "In.Country.Partner" : "in_country_partner",
    "Harvest.Year" : "harvest_year",
    "Owner.1" : "owner_1",
    "Processing.Method" : "processing_method",
    "Clean.Cup" : "clean_cup",
    "Cupper.Points" : "cupper_points",
    "Total.Cup.Points" : "total_cup_points",
    "Category.One.Defects" : "category_one_defects",
    "Category.Two.Defects" : "category_two_defects",
    "Certification.Body" : "certification_body",
    "Certification.Address" : "certification_address",
    "Certification.Contact" : "certification_contact"
}

df = df.rename(columns = rename_dict)

# Change all columns into lowercase
df.columns = df.columns.str.lower()

# Now save the dataframe into a CSV file
df.to_csv("C:/Users/TawfikAbbas/Documents/TalentPath/CapstoneProject/data/coffeequality.csv", index = False)