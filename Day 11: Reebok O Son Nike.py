############### Reebok O Son Nike Project #####################
import random

def deal_number():
  """ Returns a random number from the list."""
  numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  number = random.choice(numbers)
  return number

def calculate_score(numbers):
  """Take a list of numbers and return the score calculated from the numbers"""
  if sum(numbers) == 21 and len(numbers) == 2:
    return 0

  if 11 in numbers and sum(numbers) > 21:
    numbers.remove(11)
    numbers.append(1)
  return sum(numbers)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, computer wins with a Super Nike 😱"
  elif user_score == 0:
    return "You Win with a Super Rebok 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Computer went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(logo)

  user_numbers = []
  computer_numbers = []
  is_game_over = False

  for _ in range(2):
    user_numbers.append(deal_number())
    computer_numbers.append(deal_number())

  while not is_game_over:

    user_score = calculate_score(user_numbers)
    computer_score = calculate_score(computer_numbers)
    print(f"   current number of user - Rebok: {user_score}")
    print(f"   current number of computer - Nike: {computer_score}\n")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get more Reebok, type 'n' to pass: ")
      if user_should_deal == "y":
        user_numbers.append(deal_number())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_numbers.append(deal_number())
    computer_score = calculate_score(computer_numbers)

  print(f"\n   Your final hand: {user_numbers}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_numbers}, final score: {computer_score}\n")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play Reebok O Son Nike? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
