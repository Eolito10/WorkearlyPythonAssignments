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



# Create the horizontal bar chart
plt.figure(figsize=(12, 10))

bars = plt.barh(sales_data['store_name'], sales_data['% Sales'], color='blue')

# Invert Y-axis for better readability
plt.gca().invert_yaxis()

# Add labels to each bar
for bar in bars:
    width = bar.get_width()  # Get the width of the bar (which corresponds to %Sales)
    plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width:.2f}%',
             va='center', fontsize=12)






# Customize x and y ticks
plt.xticks(ticks=np.arange(0.0, 22.5, 2.5))  # x-axis ticks from 0 to 22.5 with step 2.5



# Add labels and title
plt.xlabel('% Sales')
plt.ylabel('Store Name')
plt.title('Percentage of Sales by Store')

# Show the plot
plt.tight_layout()
plt.show()
