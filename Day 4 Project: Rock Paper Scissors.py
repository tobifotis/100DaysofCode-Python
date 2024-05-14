rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _____________
---'   __________)__
          __________)
          ___________)
         ___________)
---.______________)
'''

scissors = '''
    _______
---'   ____)_______
          _________)
       _____________)
      (____)
---.__(___)
'''

# Your code below
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

import random

computer_choice = random.randint(0, 2)

if choice == 0:
    print("\nYou chose Rock: ")
    print(rock)
    if computer_choice == 0:
        print("Computer chose Rock:")
        print(rock)
        print("It is a tie!")
    elif computer_choice == 1:
        print("Computer chose Paper:")
        print(paper)
        print("You lose!")
    elif computer_choice == 2:
        print("Computer chose Scissors:")
        print(scissors)
        print("You win!")       
elif choice == 1:
    print("\nYou chose Paper: ")
    print(paper)
    if computer_choice == 0:
        print("Computer chose Rock:")
        print(rock)
        print("You win!")  
    elif computer_choice == 1:
        print("Computer chose Paper:")
        print(paper)
        print("It is a tie!")
    elif computer_choice == 2:
        print("Computer chose Scissors:")
        print(scissors)
        print("You lose!")  
elif choice == 2:
    print("\nYou chose Scissors: ")
    print(scissors)
    if computer_choice == 0:
        print("Computer chose Rock:")
        print(rock)
        print("You lose!")
    elif computer_choice == 1:
        print("Computer chose Paper:")
        print(paper)
        print("You win!")
    elif computer_choice == 2:
        print("Computer chose Scissors:")
        print(scissors)
        print("It is a tie!")  

