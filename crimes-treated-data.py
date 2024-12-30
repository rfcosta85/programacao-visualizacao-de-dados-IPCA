import pandas as pd

# Load CSV File
df = pd.read_csv('NYC_crime.csv')

df.info()

# Give name for the first column
df = df.rename(columns={'Unnamed: 0': 'id'})
df.info()

# select columns 
columns_to_keep = [
    'id',
    'ofns_desc',
    'age_group',
    'perp_sex',
    'perp_race',
    'latitude',
    'longitude',
    'arrest_boro',
    ':@computed_region_f5dn_yrer',
    ':@computed_region_92fq_4b7q',
]

filterd_df = df[columns_to_keep]

# Generate new CSV
output_file = 'filtered_crime_data.csv'
filterd_df.to_csv(output_file, index=False)

print(f"The modified data has been saved to {output_file}.")