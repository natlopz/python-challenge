# PyBank Challenge

import pandas as pd 

# Specifying path to CSV file
file_path = 'C:\\Users\\lnata\\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv'

# Read CSV file
df = pd.read_csv(file_path)

# Space between code and output
print(" ")

# Header
print("Financial Analysis")

# Spacer
print("------------------------------")

# Calculate total number of months included in dataset
total_months = df['Date'].nunique()

# Print total number of months
print("Total Months: " + str(total_months))

# Calculate net total amount of Profit/Losses over the entire period
net_total = df['Profit/Losses'].sum()

# Print net total of Profit/Losses
print("Total: $" + str(net_total))

# Calculate changes in Profit/Losses over the entire period
df['Profit/Losses Change'] = df['Profit/Losses'].diff()

# Calculate average
avrg = df['Profit/Losses Change'].mean()

# Print average of Profit/Losses Change
print("Average: $"+ format(avrg, '.2f'))

# Calculate greatest increase/decrease in profits
gincrease = df['Profit/Losses Change'].max()
gincrease_date = df.loc[df['Profit/Losses Change'] == gincrease, 'Date'].values[0]

gdecrease = df['Profit/Losses Change'].min()
gdecrease_date = df.loc[df['Profit/Losses Change'] == gdecrease, 'Date'].values[0]

# Print greatest increase/decrease in profits
print("Greatest Increase in Profits: " + str(gincrease_date) + " ($" + format(gincrease, '.0f') + ")")
print("Greatest Decrease in Profits: " + str(gdecrease_date) + " ($" + format(gdecrease, '.0f') + ")")

# Export!
output_file_path = 'Pybank_analysis_summary.txt'
with open(output_file_path, 'w') as file:
    file.write("Financial Analysis" + '\n')
    file.write("----------------------------" + '\n')
    file.write("Total Months: " + str(total_months) + '\n')
    file.write("Total: $" + str(net_total) + '\n')
    file.write("Average: $"+ format(avrg, '.2f') + '\n')
    file.write("Greatest Increase in Profits: " + str(gincrease_date) + " ($" + format(gincrease, '.0f') + ")" + '\n')
    file.write("Greatest Decrease in Profits: " + str(gdecrease_date) + " ($" + format(gdecrease, '.0f') + ")" + '\n')
