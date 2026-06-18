
print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? "))
tip = int(input("What is the percentage of tip you would like to give to ? 10 12 or 15? "))
split = int(input("How many people to split the bill? "))


tip_total= (float(bill * tip / 100))
total_bill = (bill + tip_total)
split_amount = (total_bill / split)
the_total = (split_amount)

# print((the_total), "is your total amount")

print(f"{split_amount:.2f} is your total amount")



# f":.2f" {}

# sally_mae = it(input("How much is the tip? "))

# print(sally_mae)