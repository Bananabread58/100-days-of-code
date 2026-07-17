small = 15
medium = 20
large = 25
bill = 0 
pepperonismall = 2
pepperoniregular = 3
extracheese = 1


print("Welcome to tupac's pizza")
order = (input("Would you like a pizza? y/n "))
tupac_order = print(order)

if order == "y":
    size = (input("What size would you like? small, medium, or large?  "))
    if size == "small": 
        bill = small
    elif size == "medium":
       bill = medium 
    elif size == "large":
        bill = large
        print(bill)
    toppings = (input("Would you like pepperoni? "))
    if toppings == "y" and size == "small":
        bill = bill + pepperonismall
    elif toppings == "y" and size == "medium":
        bill = bill + pepperoniregular
    elif toppings == "y" and size == "large":
        bill = bill + pepperoniregular
    else: 
       print("No toppings")
    toppings2 = (input("Would you like extra cheese with that "))
    if toppings2 == "y": 
        bill = bill + extracheese    
    else: 
        print("No extra cheese")

else:
  print("You didn't order anything. Please Order Something OR GET OUT!")


print(f"Your total is {bill} ")

     
   
    


