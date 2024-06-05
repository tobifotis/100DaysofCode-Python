import random

top_of_range = int(input("Type a number: "))

random_number = random.randint(1, top_of_range)
print(f"Random number is = {random_number}")

num_guesses = 0

while True:
  num_guesses += 1
  guess = int(input("Guess the random number: "))
  if guess <= 0:
    print("Please, Type a number larger than 0 next time. ")
    continue

  if guess == random_number:
    print("You got it!")
    break
  else:
    if guess > random_number:
      print("You guess is ABOVE the number!")
    else:
      print("You guess is BELOW the number!")

print(f"You got it on your {num_guesses}th attempt!")



