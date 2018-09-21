<<<<<<< HEAD
import csv
import os

file = "budget_data.csv"

list_months = []
total_revenue = 0
revenue_list = []
monthly_changes = []
monthly_increases = []
total_monthly_rev_change = 0

with open(file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for (row) in reader:
        current_month = row["Date"]
        current_revenue = int(row["Profit/Losses"])
        list_months.append(current_month)
        revenue_list.append(current_revenue)
        total_revenue = total_revenue + current_revenue

for i in range(0, len(revenue_list)-1):
    month_change = revenue_list[i+1] - revenue_list[i]
    monthly_changes.append(month_change)
    total_monthly_rev_change= total_monthly_rev_change + month_change
    
print("Financial Analysis")
print("------------------")
print(f'Total Months: {len(list_months)}')
print(f"Net Profit/Loss: {total_revenue}")
print(f'Average Profit/Loss Change: {total_monthly_rev_change / len(monthly_changes)}')
print(f'Greatest Profit:  {list_months[monthly_changes.index(max(monthly_changes)) + 1]} {max(monthly_changes)}')
print(f'Greatest Loss: {list_months[monthly_changes.index(min(monthly_changes)) + 1]}  {min(monthly_changes)}')

budget_data = open("Results.txt", "w")
budget_data.write("Financial Analysis \n") 
budget_data.write(f'Total Months: {len(list_months)} \n')
budget_data.write(f'Net Profit/Loss: {total_revenue} \n')
budget_data.write(f'Average Profit/Loss Change: {total_monthly_rev_change / len(monthly_changes)} \n')
budget_data.write(f'Greatest Profit:  {list_months[monthly_changes.index(max(monthly_changes)) + 1]} {max(monthly_changes)} \n')
budget_data.write(f'Greatest Loss: {list_months[monthly_changes.index(min(monthly_changes)) + 1]}  {min(monthly_changes)}')
=======

>>>>>>> 83f9b72a436c2c2a6af1cd26935dd484e5c5a472
