import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Group by zip_code and item_number to calculate total bottles sold
merged_df = selected_columns.groupby(['zip_code', 'item_number'], as_index=False)['bottles_sold'].sum()


# Sort by bottles_sold in descending order to get the top 5
top_5_df = merged_df.sort_values(by='bottles_sold', ascending=False).head(5)

top_5_rows = merged_df.head(5)

# Add index positions for plotting
merged_df['index_pos'] = np.arange(len(merged_df))

# Prepare data for plotting
x = merged_df['index_pos']                     # X-axis: position in sorted data
y = merged_df['bottles_sold']                  # Y-axis: bottles sold
sizes = merged_df['bottles_sold'] * 1       # Scale the marker sizes (adjust multiplier for better visualization)
colors = plt.cm.viridis(np.linspace(0, 1, len(merged_df)))  # Color gradient for aesthetics

# Create the scatter plot
scatter=sns.scatterplot(x=x, y=y)



# Adjust x-axis to reflect the correct number of positions
for i in top_5_rows.index:  # Use the indices of the top 5 rows
    plt.text(
        top_5_df.index[i],  # x position
        top_5_df['bottles_sold'].iloc[i],  # y position
        str(top_5_df['item_number'].iloc[i]),  # label (e.g., item_number)
        fontsize=8, ha='right', va='bottom', color='black'
    )


# Add labels and title
plt.xlabel('Index', fontsize=12)
plt.ylabel('Bottles Sold', fontsize=12)
plt.title('Bottles sold', fontsize=14)




# Customize x and y ticks
plt.xticks(ticks=np.arange(0, 80, 20))  # x-axis ticks from 0 to 60 with step 20
plt.yticks(ticks=np.arange(0, 1600, 500))  # y-axis ticks from 0 to 1500 with step 500





# Show the plot
plt.show()

# Create the scatter plot







