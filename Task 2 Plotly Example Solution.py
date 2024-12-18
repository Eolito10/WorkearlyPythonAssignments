import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize, LinearSegmentedColormap

# Read in the data
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter by date range
start_date = '01/01/2016'
end_date = '31/12/2019'
df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# Calculate % Sales
df_filtered['% Sales'] = (df_filtered['sale_dollars'] / df_filtered['sale_dollars'].sum()) * 100

# Group by store_name to aggregate %Sales (in case there are duplicates)
sales_data = df_filtered.groupby('store_name', as_index=False)['% Sales'].sum()

# Sort by %Sales in descending order for better visualization
sales_data = sales_data.sort_values(by='% Sales', ascending=False).head(15)

# Normalize the %Sales data for color mapping
norm = Normalize(vmin=sales_data['% Sales'].min(), vmax=sales_data['% Sales'].max())

# Define a custom colormap (blue to yellow)
custom_cmap = LinearSegmentedColormap.from_list('blue_to_yellow', ['blue', 'purple', 'yellow'])

# Create the horizontal bar chart
plt.figure(figsize=(12, 10))
colors = custom_cmap(norm(sales_data['% Sales']))
bars = plt.barh(sales_data['store_name'], sales_data['% Sales'], color=colors)

# Invert Y-axis for better readability
plt.gca().invert_yaxis()

# Add labels to each bar
for bar in bars:
    width = bar.get_width()  # Get the width of the bar (which corresponds to %Sales)
    plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width:.2f}%',
             va='center', fontsize=12)

# Add a color bar
sm = cm.ScalarMappable(cmap=custom_cmap, norm=norm)
sm.set_array([])  # Add an empty array for the color bar
cbar = plt.colorbar(sm, orientation='vertical', ax=plt.gca())

# Customize the color bar ticks
tick_locations = np.arange(0, 20, 5)  # Tick locations from 0 to 20 with step 5
cbar.set_ticks(tick_locations)        # Set the tick locations
cbar.set_ticklabels(tick_locations)  # Set the tick labels (e.g., '0%', '5%')

# Set the label of the color bar on the top
cbar.ax.set_xlabel('% Sales', fontsize=12, labelpad=10)  # Move the label above the color bar
cbar.ax.xaxis.set_label_position('top')  # Position the label at the top

# Customize x and y ticks
plt.xticks(ticks=np.arange(0.0, 22.5, 2.5))  # x-axis ticks from 0 to 22.5 with step 2.5



# Add labels and title
plt.xlabel('% Sales')
plt.ylabel('Store Name')
plt.title('Percentage of Sales by Store')

# Show the plot
plt.tight_layout()
plt.show()
