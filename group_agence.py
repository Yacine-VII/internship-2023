import pandas as pd

# Read data from the file and create a DataFrame
df = pd.read_csv("ref_agences.txt", sep=';', encoding='utf-8')

# Group data by "Direction Générale" and get the unique "ID_AGENCE" for each group
grouped_data = df.groupby("DIRECTION_GENERALE")["ID_AGENCE"].unique().reset_index()

# Save the grouped data to a text file
grouped_data.to_csv("grouped_data.txt", sep='\t', index=False)

print("Data saved to grouped_data.txt")

