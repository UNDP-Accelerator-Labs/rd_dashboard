import pandas as pd
import json
import os

# Load the Excel file
file_path = 'R&D_dashboard_data.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Prepare the data

# Count of R&D activities per country
activities_per_country = df['country'].value_counts().reset_index()
activities_per_country.columns = ['Country', 'Number of Activities']

# Count of themes across countries (instead of regions)
themes_per_country = df.groupby(['country', 'Theme']).size().unstack(fill_value=0)

# Distribution of topics across themes
topics_per_theme = df.groupby('Theme')['topic'].value_counts().unstack(fill_value=0)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')


# Ensure the _data directory exists
output_dir = '_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the JSON data to a file
with open(os.path.join(output_dir, 'rd_data.json'), 'w') as json_file:
    json_file.write(json_data)

# Save the processed data to JSON files
activities_per_country.to_json('_data/activities_per_country.json', orient='records')
themes_per_country.to_json('_data/themes_per_country.json', orient='split')  # Update the file name
topics_per_theme.to_json('_data/topics_per_theme.json', orient='split')

# Count the number of occurrences of each theme
theme_counts = df['Theme'].value_counts().reset_index()
theme_counts.columns = ['Theme', 'Number of Activities']

# Save the processed data to JSON files
theme_counts.to_json('_data/theme_counts.json', orient='records')