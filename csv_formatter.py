import pandas as pd

# Input lists
data_fund = pd.read_csv('Input file - 1.csv')
data_objects = pd.read_csv('Input file - 2.csv')

# Merge 2 tables with key object and object_code
merged_data = pd.merge(data_fund, data_objects, left_on='Object', right_on='Object_Code')

# Change data, so every year becomes the new row with value
reshaped_data = merged_data.melt(id_vars=['Fund', 'Department', 'Object', 'Object_Name', 'Object_Type'],
                                 value_vars=['Actual 2022', 'Actual 2023', 'Actual 2024'],
                                 var_name='Year', value_name='Value')

# Handle year correctly and add minus to R values
reshaped_data['Year'] = reshaped_data['Year'].str.extract(r'(\d{4})')
reshaped_data.loc[reshaped_data['Object_Type'] == 'R', 'Value'] *= -1

# Grouping data
final_data = reshaped_data.groupby(['Fund', 'Department', 'Object', 'Year'], as_index=False).sum()

# Save in CSV
final_data[['Fund', 'Department', 'Object', 'Year', 'Value']].to_csv('/mnt/data/processed_output.csv', index=False)
