import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter by date range
start_date = '01/01/2016'
end_date = '31/12/2019'
df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# Select relevant columns
selected_columns = df_filtered[['zip_code', 'item_number', 'bottles_sold']]

# Sort by zip_code
sorted_sc = selected_columns.sort_values(by='zip_code', ascending=True)

# Group by zip_code and item_number to calculate total bottles sold
merged_df = sorted_sc.groupby(['zip_code', 'item_number'], as_index=False)['bottles_sold'].sum()

# Sort by bottles_sold in descending order to get the top 5
top_5_df = merged_df.sort_values(by='bottles_sold', ascending=False).head(5)





# Generate colors for the scatter plot
colors = plt.cm.viridis(np.linspace(0, 1, len(merged_df)))

# Prepare x and y for the scatter plot
x = merged_df.index   # Use the index as x
y = merged_df['bottles_sold']
k = merged_df['item_number']

top_5_rows = merged_df.head(5)

# Create the scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(x, y, c=colors, alpha=0.8)


# Adjust x-axis to reflect the correct number of positions
for i in top_5_rows.index:  # Use the indices of the top 5 rows
    plt.text(
        top_5_df.index[i],  # x position
        top_5_df['bottles_sold'].iloc[i],  # y position
        str(top_5_df['item_number'].iloc[i]),  # label (e.g., item_number)
        fontsize=8, ha='right', va='bottom', color='black'
    )

# Add labels and title
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Scatter Plot: Bottles Sold')

# Show the plot
plt.show()
