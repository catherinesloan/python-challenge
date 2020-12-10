import os 
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")
# Read in the CSV file
with open(budget_csv, "r") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header
    next(csvreader, None)

    # Declare variables as empty lists
    months = []
    revenue = []
    revenue_changes = []

    # Loop through the data
    for row in csvreader:
        
        # Add csv value to the empty list created above
        months.append(row[0])
        # Count the length of this list to calculate the total number of months - line 54

        # Add csv value to the empty list created above
        revenue.append(int(row[1]))
        # Use sum function to calculate the net total amount of profit/losses - line 55

    # Create a for loop using length of revenue list for range
    for i in range(len(revenue)-1):
        
        # Add formula for calculating revenue changes to empty list
        revenue_changes.append(revenue[i+1] - revenue[i])
        # Calculate the average change using the sum of the above / total number of changes
        average_change = sum(revenue_changes) / len(revenue_changes)
        # Add this to the financial analysis below, rounding to 2dp - line 56
        
        # Use the maximum function to calculate greatest increase
        greatest_increase = max (revenue_changes)
        # Assign the month adding 1, otherwise it took name for previous month
        month_increase = months[revenue_changes.index(greatest_increase)+1]
        # Add both of these to the financial analysis below - line 57

        # Do same again but with the minimum function to calc greatest decrease
        greatest_decrease = min (revenue_changes)
        # Assign the month adding 1, otherwise it took name for previous month
        month_decrease = months[revenue_changes.index(greatest_decrease)+1]
        # Add both of these to the financial analysis below - line 58


# Print out the financial analysis to terminal
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(revenue)}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {month_increase} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {month_decrease} ${greatest_decrease}")


# Export the above analysis as a text file in analysis folder
f = open("Analysis/financial_analysis.txt", "w" )
f.write(
    "Financial Analaysis\n"
    "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
    f"Total Months: {len(months)}\n"
    f"Total: ${sum(revenue)}\n"
    f"Average Change: ${round(average_change,2)}\n"
    f"Greatest Increase in Profits: {month_increase} ${greatest_increase}\n"
    f"Greatest Decrease in Profits: {month_decrease} ${greatest_decrease}\n"
    )