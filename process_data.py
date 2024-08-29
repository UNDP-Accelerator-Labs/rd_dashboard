import pandas as pd
import json
import os

# Load the JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Convert JSON data to a DataFrame
df = pd.DataFrame(data)

# Replace empty or NaN values in the 'R&D cycle' column with 'Unknown'
df['R&D cycle'] = df['R&D cycle'].replace('', 'Unknown')
df['R&D cycle'] = df['R&D cycle'].fillna('Unknown')

# Count the connections between each Theme and Region for Sankey diagram
theme_region_counts = df.groupby(['Theme', 'region']).size().reset_index(name='counts')

# Prepare data for Sankey diagram
themes = df['Theme'].unique().tolist()
regions = df['region'].unique().tolist()

# Create source, target, and value lists
source = theme_region_counts['Theme'].apply(lambda x: themes.index(x)).tolist()
target = theme_region_counts['region'].apply(lambda x: len(themes) + regions.index(x)).tolist()
value = theme_region_counts['counts'].tolist()

# Prepare the final data structure for Sankey
sankey_data = {
    "nodes": {
        "label": themes + regions,
    },
    "links": {
        "source": source,
        "target": target,
        "value": value
    }
}

# Process the data for a stacked bar chart
stacked_data = df.groupby(['Theme', 'region']).size().unstack(fill_value=0).reset_index()

# Convert the processed data to a JSON format
stacked_data_json = stacked_data.to_json(orient='split')

# Convert the DataFrame to JSON and save it to _data folder
output_dir = '_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, 'sankey_data.json'), 'w') as json_file:
    json.dump(sankey_data, json_file)

with open(os.path.join(output_dir, 'stacked_bar_data.json'), 'w') as json_file:
    json.dump(stacked_data_json, json_file)

# Group by theme and count the number of activities (or labs)
theme_counts = df['Theme'].value_counts().reset_index()
theme_counts.columns = ['Theme', 'Number of Labs']

# Convert the processed data to JSON format
theme_counts_json = theme_counts.to_json(orient='records')

# Save the JSON data to a file
with open(os.path.join(output_dir, 'gauge_chart_data.json'), 'w') as json_file:
    json.dump(theme_counts_json, json_file)


# Process the data for a stacked bar chart
stacked_data_category = df.groupby(['Theme', 'R&D cycle']).size().unstack(fill_value=0).reset_index()

# Convert the processed data to a JSON format
stacked_data_category__json = stacked_data_category.to_json(orient='split')

# Save the processed data to the _data folder
with open(os.path.join(output_dir, 'stacked_bar_chart_category_data.json'), 'w') as json_file:
    json.dump(stacked_data_category__json, json_file)
