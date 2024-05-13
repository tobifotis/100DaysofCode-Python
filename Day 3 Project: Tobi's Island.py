print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tobi's Island!")
print("Your mission is to find the \"Vibranium\".\n")
choice1 = input('You are at a cross road, Where do you want to go? "left" or "right" \n').lower()

if choice1 == "left":
  choice2 = input('\nYou find yourself in front of a lake. Wakanda island is in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input('\nYou arrive at Wakanda island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? \n').lower()
    if choice3 == "red":
      print("You got burned by Fire. Game Over!")
    elif choice3 == "blue":
      print("You have entered a room full of beasts. Game Over!")
    elif choice3 == "yellow":
      print("\nYou have found the Vibranium. You Win!")
    else: 
      print("Game Over!")
  else:
    print("You got attacked by an Alligator. Game over!")
else:
  print("You fell into a well. Game over!")