# Import modules os and csv

import os
import csv

# Set the path for the CSV file

PyBankcsv = os.path.join("Resources","budget_data.csv")


# Create lists to store data

profit = []
monthly_changes = []
date = []

# Initialize the variables
 
total_months = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the CSV using the set path

with open(PyBankcsv, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)

    # Conducting the ask
    for row in csv_reader:    
      # Use total_months to count the number of months in this dataset
      total_months = total_months + 1 

      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      # Calculate the average change in profits month on month
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      # Store the monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      # Calculate the average change in profits
      average_change_profits = (total_change_profits/total_months)
      
      # Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    print("----------------------------------------------------------")
    print(" Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('analysis/financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write(" •    Total Months: " + str(total_months) + "\n")
    text.write(" •    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write(" •    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write(" •   Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write(" •   Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")