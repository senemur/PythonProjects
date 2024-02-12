print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
# if tip_percentage != 10 and 12 and 15:
#     print("Please enter a valid tip percentage.")
_people = int(input("How many people to split the bill? "))
tip_amount = total_bill + total_bill * (tip_percentage / 100)
total_tip = tip_amount / _people
end_ = round(total_tip, 2)
end_ = "{:.2f}".format(total_tip)
print(f"Each person's tip amount is ${end_}")
