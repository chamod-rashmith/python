"""
Lesson 6: Advanced Pandas
Concepts: GroupBy, Merging, Pivot Tables.
Why? In ML, you often need to aggregate stats (e.g., average spend per user) before modeling.
"""
import pandas as pd
import numpy as np

# Create complex dummy data
data = {
    'Store': ['Main', 'Main', 'South', 'South', 'North', 'Main'],
    'Category': ['Electronics', 'Grocery', 'Electronics', 'Grocery', 'Grocery', 'Electronics'],
    'Sales': [1200, 450, 800, 300, 500, 1500],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-04'])
}
df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)

# 1. GroupBy: Aggregate data
print("\n--- Sales per Store ---")
store_sales = df.groupby('Store')['Sales'].sum()
print(store_sales)

# 2. Pivot Table: Heatmap-style view
print("\n--- Pivot Table (Store vs Category) ---")
pivot = df.pivot_table(values='Sales', index='Store', columns='Category', aggfunc='mean')
print(pivot)

# 3. Merging (Joining DataFrames)
other_data = pd.DataFrame({
    'Store': ['Main', 'South', 'North'],
    'Region': ['Metro', 'Suburban', 'Rural']
})

merged_df = pd.merge(df, other_data, on='Store')
print("\n--- Merged Data (Adding Regions) ---")
print(merged_df)

print("\n--- ML Tip ---")
print("We use GroupBy for 'Feature Engineering'—creating new features about the data's structure.")
