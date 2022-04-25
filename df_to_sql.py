# Install psycopg2: it's already been installed in the local environment
#pip install psycopg2

# Library imports 
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine

# Create an engine instance 
engine = create_engine('postgresql+psycopg2://postgres:1066@localhost:5432/coffeequality')

conn = engine.connect()

table = "coffee"

# Read in the csv to a pandas dataframe

df = pd.read_csv("C:/Users/TawfikAbbas/Documents/TalentPath/CapstoneProject/data/coffeequality.csv")

# Create the table if it does not exist and read in the rows, then close the connection afterwards
try:    
    frame = df.to_sql(table, conn, if_exists= 'fail')

except ValueError as vx:
    print("A", vx)

except Exception as ex:
    print("B", ex)
else:
    print("PostgreSQL Table %s has been created successfully."%table)
finally:
    conn.close()

