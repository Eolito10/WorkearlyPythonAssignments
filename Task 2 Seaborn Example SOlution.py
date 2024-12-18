import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LinearSegmentedColormap
import seaborn as sns

# Read in the data
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter by date range
start_date = '01/01/2016'
end_date = '31/12/2019'
df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# Filter by date range and create a copy to avoid warnings
df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)].copy()

# Calculate % Sales
df_filtered['% Sales'] = (df_filtered['sale_dollars'] / df_filtered['sale_dollars'].sum()) * 100



# Group by store_name to aggregate %Sales (in case there are duplicates)
sales_data = df_filtered.groupby('store_name', as_index=False)['% Sales'].sum()

# Sort by %Sales in ascending order and select top 15
sales_data = sales_data.sort_values(by='% Sales', ascending=True).tail(15)

# Normalize the %Sales data for color mapping
norm = Normalize(vmin=sales_data['% Sales'].min(), vmax=sales_data['% Sales'].max())

# Define a custom colormap
custom_cmap = LinearSegmentedColormap.from_list('blue_to_yellow', ['pink', 'green', 'blue', 'pink'])

# Generate color palette based on normalized % Sales
colors = [custom_cmap(norm(value)) for value in sales_data['% Sales']]

# Create the horizontal bar chart using Seaborn
plt.figure(figsize=(12, 10))
sns.barplot(
    x='% Sales',
    y='store_name',
    data=sales_data,
    hue='store_name',  # Use `store_name` as the hue variable
    palette=colors,    # Apply the custom color palette
    dodge=False,       # Ensure no offset between bars
    legend=False       # Suppress the legend
)

# Add labels to each bar
for i, value in enumerate(sales_data['% Sales']):
    plt.text(value + 0.5, i, f'{value:.2f}%', va='center', fontsize=12)

# Add labels and title
plt.xlabel('% Sales')
plt.ylabel('Store Name')
plt.title('Percentage of Sales by Store')

# Tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
