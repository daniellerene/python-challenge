import pandas as pd

# Read CSV file
df = pd.read_csv('python-challenge/PyBank/Resources/budget_data.csv')

# Calculate total number of months included in the dataset
total_months = len(df.index)

# Calculate net total amount of "Profit/Losses"
total_profit_losses = df['Profit/Losses'].sum()

# Calculate changes in "Profit/Losses" over the entire period
df['Volume Change'] = df['Profit/Losses'].diff()

# Calculate total average of the changes
total_average_change = df['Volume Change'].mean().round(2)

# Calculate greatest increase in profits (date and amount)
greatest_increase_row = df.loc[df['Volume Change'].idxmax()]
greatest_increase_amount = df['Volume Change'].max().astype(int)

# Calculate greatest decrease in profits (date and amount)
greatest_decrease_row= df.loc[df['Volume Change'].idxmin()]
greatest_decrease_amount = df['Volume Change'].min().astype(int)

# Uncomment below block to print output to terminal
# print("Total Months:", total_months)
# print("Total: $", total_profit_losses)
# print("Average Change: $", total_average_change)
# print("Greatest Increase in Profits:", greatest_increase_row['Date'], "($", greatest_increase_amount,")")
# print("Greatest Decrease in Profits:", greatest_decrease_row['Date'], "($", greatest_decrease_amount,")")

with open("python-challenge/PyBank/analysis/financial_analysis.txt", "w") as text_file:
    # text_file.write("Total Months: %s \n" % total_months)
    # text_file.write("Total: %s \n" % total_profit_losses)
    # text_file.write("Greatest Increase in Profits: %s \n" % greatest_increase_row['Date'])
    # text_file.write("Greatest Increase in Profits: %s" % greatest_increase_row['Date'])
    # text_file.write("Greatest Decrease in Profits: %s \n" % greatest_decrease_row['Date'])

    text_file.writelines([
        ("Financial Analysis\n"),
        ("------------------\n"),
        ("Total Months: %s \n" % total_months),
        ("Total: $%d \n" % total_profit_losses),
        ("Average Change: $%.2f \n" % total_average_change),
        ("Greatest Increase in Profits: %s ($%d)\n" % (greatest_increase_row['Date'], greatest_increase_amount)),
        ("Greatest Decrease in Profits: %s ($%d)" % (greatest_decrease_row['Date'], greatest_decrease_amount))
        ])