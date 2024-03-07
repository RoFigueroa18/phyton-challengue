import csv
import os
file_path = os.path.join("Resources", "budget_data.csv")

# Function to analyze financial records
def analyze_financial_records(file_path):
    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    profit_loss_changes = ()
    dates = ()

    # Read the CSV file
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Skip the header row
        next(csvreader)

        # Loop through each row in the CSV
        for row in csvreader:
            # Extract date and profit/loss values
            date = row[0]
            profit_loss = int(row[1])

            # Calculate total months and net total
            total_months += 1
            net_total += profit_loss

            # Calculate profit/loss changes
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                profit_loss_changes.append(change)
                dates.append(date)

            # Update previous profit/loss
            previous_profit_loss = profit_loss

    # Calculate average change
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)

    # Find the greatest increase and decrease
    greatest_increase = max(profit_loss_changes)
    greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
    greatest_decrease = min(profit_loss_changes)
    greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

    # Display results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Specify the path to the CSV file
file_path = os.path.join("Resources", "budget_data.csv")

# Call the function with the file path
analyze_financial_records(file_path)