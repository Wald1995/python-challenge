# Module 3 Challenge (PyBank)

# Instructions / delivery:
#       1.	The total number of months included in the dataset
#       2.	The total net amount of "Profit/Losses" over the entire period
#       3.	The changes in "Profit/Losses" over the entire period, and then the average of those changes
#       4.	The greatest increase in profits (date and amount) over the entire period
#       5.	The greatest decrease in profits (date and amount) over the entire period

# Import modules
import os, csv

# create the path for the csv file
csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "Financial_Analysi_PyBank.txt")

# Create the list that we are going to use
date = []
profit = []
monthly_change_list =[]

# Create Variables
count_months = 0
total_amount = 0
total_monthly_change = 0
previous_profit_losses = 0

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:      
        # append the information for the corresponding calculations in the future
        date.append(row[0])
        profit.append(int(row[1]))

# 1. Calculate the quantity of months
count_months = len(date)
      
# 2. Calculate the total amount (profit/losses)
total_amount = sum(profit)

# 3.1 Calculate the changes in "Profit/Losses" over the entire period 
for i in range(1, len(profit)):
    monthly_change_list.append(profit[i] - profit[i-1])

# 3.2 Calculate the average 
average_monthly_change = (sum(monthly_change_list)/len(monthly_change_list))
    
# 4. Find the max change in profits
greatest_increase = max(monthly_change_list)
increase_date = date[monthly_change_list.index(greatest_increase)+1]

# 5. Find the min change in profits
greatest_decrease = min(monthly_change_list)
decrease_date = date[monthly_change_list.index(greatest_decrease)+1]
        
# Print the results:
print(f'\nFinancial Analysis\n')
print(f'---------------------------------------------------\n')
print(f'Total Months: {count_months}\n')
print(f'Total: {total_amount}\n')
print(f'Average Change: ${round(average_monthly_change,2)}\n')
print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase})\n')
print(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})')

with open(output_path, 'w') as text:
    text.write("Financial Analysis PyBank\n")
    text.write("----------------------------------------\n")
    text.write(f'Total Months: {count_months}\n')
    text.write(f'Total: ${total_amount}\n')
    text.write(f'Average Change: ${round(average_monthly_change,2)}\n')
    text.write(f'Greatest Increase in Profits: {increase_date} (${greatest_increase})\n')
    text.write(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})')
