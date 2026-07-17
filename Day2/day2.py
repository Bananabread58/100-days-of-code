print("Calculator for tips!")
bill = float(input("What was your total bill?"))
tip = int(input("Whats the percentage of tip you would like to give? 10 12 or 15"))
people = int(input("How many people split the bill?"))
tip_with_percent = tip / 100
total_tip = bill * tip_with_percent
total_bill = bill + total_tip
bill_with_others = total_bill / people 
final_total = round (bill_with_others, 2)
print(f"Each person should pay: ${final_total} ")