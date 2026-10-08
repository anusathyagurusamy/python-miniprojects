# Simple Expense Tracker (CSV)
import csv

choice = input("1. Add Expense 2. View Total: ")

if choice == "1":
    item = input("Item: ")
    amount = input("Amount: ")

    with open("expenses.csv", "a", newline="") as f:
        csv.writer(f).writerow([item, amount])

else:
    with open("expenses.csv", "r") as f:
        total = sum(float(row[1])
                    for row in csv.reader(f))

    print(f"Total spent: ₹{total}")