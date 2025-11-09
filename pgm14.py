"""
Take as inputs, the months and profits made by a company ABC over a year.
Represent this data using a line plot. The genrated line plot must include X-Axis label:
"Month number" and Y-Axis label: "Total Profit"
"""
import matplotlib.pyplot as plt

month = list(map(int, input("Enter the month numbers(1 - 12): ").split()))
totalProfit = list(map(int, input("Enter corresponding profits: ").split()))

plt.plot(month, totalProfit, marker="o", linestyle="-", color="b")
plt.title("Company ABC Profits Over a Year")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()
