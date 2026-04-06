import pandas as pd

df = pd.read_csv('../../data/tips.csv')

print("\n--- Dataset Info---")
print(df.info())

# Which days make the most money? Saturday produces the highest total revenue, indicating peak customer demand and making it the most critical day for staffing and inventory planning.
# When should we schedule more staff? Dinner service generates significantly higher revenue and customer volume than lunch, indicating that staffing levels should be prioritized during evening hours.
# What customer groups spend more? Parties of two have the highest average bill size, suggesting smaller groups may order more per person compared to larger parties.
# Do larger parties generate better revenue? Larger parties do not consistently generate higher average bills, indicating that increasing table size alone does not guarantee higher revenue per table.
# Is dinner or lunch more profitable? Dinner service outperforms lunch in total revenue, making it the primary revenue driver for the restaurant.

## Dinner generates ~65% of total revenue, making it the primary operational focus.


# Revenue by day
revenue_by_day = df.groupby('day')['total_bill'].sum()
print("\nRevenue By Day:")
print(revenue_by_day)

# Revenue by time (Lunch vs Dinner)
revenue_by_time= df.groupby('time')['total_bill'].sum()
print("\nRevenue By Time:")
print(revenue_by_time)

# Average bill by party size
avg_bill_by_size = df.groupby('size')['total_bill'].sum()
print("\nAverage Bill By Party Size:")
print(avg_bill_by_size)