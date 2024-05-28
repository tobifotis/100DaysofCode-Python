from art import logo
print(logo)
import random
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.\n")
rand_num = random.randint(1, 101)
# print(f"The correct answer is {rand_num}")
difficulty = input("\nChoose a difficulty. Type 'easy' or 'Hard': ").lower()

def num_lives(difficulty):
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
count = num_lives(difficulty)

finished = False
while not finished:
  print(f"You have {count} attempts remaining to guess the number. ")
  count -= 1
  guess = int(input("Make a guess: "))
  if guess < rand_num:
    print("\n Too Low!")
    print(" Guess again.")
  elif guess > rand_num:
    print("\n Too High!")
    print(" Guess again.")
  elif guess == rand_num:
    print(f"\n You got it! The answer was {rand_num}")
    finished = True
  if count <= 0:
    print("\n You've run out of guesses! You Lose")
    print(f" The answer was {rand_num}")
    finished = True
