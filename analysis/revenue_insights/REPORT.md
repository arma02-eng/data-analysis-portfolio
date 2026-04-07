# Revenue Insights Analysis — Restaurant Tips Dataset

## Objective

Analyze restaurant transaction data to understand revenue patterns, customer behavior, and operational insights that could help improve staffing and business decisions.

---

## Dataset

The dataset contains 244 restaurant transactions including:

* Total bill amount
* Tip amount
* Customer gender
* Smoking status
* Day of visit
* Meal time (Lunch/Dinner)
* Party size

---

## Key Metrics Created

To better evaluate performance, additional metrics were derived:

* **Tip Percentage** = tip / total_bill
* **Revenue per Person** = total_bill / party size

These metrics allow comparison of customer value rather than raw totals.

---

## Key Findings

### 1. Revenue by Day

Saturday generates the highest total revenue, indicating peak demand during weekends.

**Business implication:**
More staff and inventory should be allocated on Saturdays.

---

### 2. Lunch vs Dinner Performance

Dinner service produces significantly higher total revenue than lunch.

**Insight:**
Higher earnings are driven mainly by customer volume rather than higher spending per person.

---

### 3. Customer Spending Behavior

Smaller parties (especially size 2) show higher average bills compared to larger groups.

**Implication:**
Large parties do not necessarily increase per-customer profitability.

---

### 4. Revenue Efficiency

Revenue per person varies across days, suggesting some days attract higher-value customers rather than just higher traffic.

---

### 5. Tipping Patterns

Average tip percentage differs between meal times, indicating behavioral differences in customer tipping habits.

---

## Visualizations

Charts generated during analysis:

* Revenue by day
* Tips by gender
* Tips by party size

All visual outputs are stored locally within the project.

---

## Tools Used

* Python
* Pandas
* Matplotlib

---

## Conclusion

The analysis shows that restaurant revenue is primarily influenced by timing and customer volume rather than party size alone. Dinner service and weekend operations represent the strongest opportunities for revenue optimization through staffing and operational planning.

---

## Future Improvements

* Add time-series trend analysis
* Compare smoker vs non-smoker spending behavior
* Build predictive model for expected revenue
