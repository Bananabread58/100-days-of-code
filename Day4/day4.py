import random
rock = 0
paper = 1
scissors = 2

thechoice = int(input(("What do you choose? Rock(0), paper(1), or scissors?(2)")))
decisions = (random.choice([0, 1, 2]))

if decisions == rock and thechoice == scissors: 
   print("You lose, rock beats scissors")
elif decisions == rock and thechoice == paper: 
   print("You win paper beats rock")
# elif decisions == rock and thechoice == rock:
#    print("Tie")
elif decisions == paper and thechoice == rock:
   print("You lose, paper beats rock")
elif decisions == paper and thechoice == scissors: 
   print("You win, scissors beats rock ")
# elif decisions == paper and thechoice == paper:
#    print("Tie")
elif decisions == scissors and thechoice == paper:
   print("You lose, scissors beats paper")
elif decisions == scissors and thechoice == rock:
   print("You win, rock beats scissors")
# elif decisions == scissors and thechoice == scissors:
#    print ("Tie")
elif decisions == thechoice:
   print("tie")
else: 
   print("Type in a answer")







      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      #crazy? I was crazy once they locked me in a room a rubber room, a rubber room filled with rats and rats make me crazy