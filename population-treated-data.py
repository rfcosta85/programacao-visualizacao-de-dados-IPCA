import pandas as pd

# Load the Excel file
file_path = 'co-est2023-chg-36.xlsx'
df = pd.read_excel(file_path, skiprows=[1,2,3,4,5,66,67,68,69,70,71,72,73,74,75,76])

# Define the required columns
required_columns = [
    'Geographic Area',
    '2020 Estimates Base',
    'Population Estimate 2020',
    'Population Estimate 2021',
    'Population Estimate 2022',
    'Population Estimate 2023',
    'State Ranking of Counties 2020 Estimates Base',
    'State Ranking of Counties Population Estimate 2020',
    'State Ranking of Counties Population Estimate 2021',
    'State Ranking of Counties Population Estimate 2022',
    'State Ranking of Counties Population Estimate 2023',
    'Annual Change, 2022 to 2023 number',
    'Annual Change, 2022 to 2023 percent',
    'Cumulative Change, 2020 to 2023 Number',
    'Cumulative Change, 2020 to 2023 Percent',
    'State Ranking of Counties Annual Change, 2022 to 2023 Number',
    'State Ranking of Counties Annual Change, 2022 to 2023 Percent',
    'State Ranking of Counties Annual Change, 2020 to 2023 Number',
    'State Ranking of Counties Annual Change, 2020 to 2023 Percent',
]

# Sanatize

# Assign the required columns as the new header
df.columns = required_columns

# Remove white space and dot of the begin of the states and countys
df['Geographic Area'] = df['Geographic Area'].str.lstrip('.')

# Remove state name, of county name
df['Geographic Area'] = df['Geographic Area'].str.split(', ').str[0]

# Save the modified dataframe to a new Excel file
output_file_path = 'Ny-population-estimative-2020-23.xlsx'
df.to_excel(output_file_path, index=False)

print(f"The modified data has been saved to {output_file_path}.")

# Create File with 500k maximum population filter

# Load Excel File
df = pd.read_excel('Ny-population-estimative-2020-23.xlsx')

# Remove all cities with less than 500k of population
df = df[df['Population Estimate 2020'] >= 500000]
df = df[df['Population Estimate 2021'] >= 500000]
df = df[df['Population Estimate 2022'] >= 500000]
df = df[df['Population Estimate 2023'] >= 500000]

# Save the modified dataframe to a new Exel file
output_file_path = 'Ny-population-estimative-2020-23-500k.xlsx'
df.to_excel(output_file_path, index=False)

print(f"The modified data has been saved to {output_file_path}.")
