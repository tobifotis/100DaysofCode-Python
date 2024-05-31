MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "coffee": 18,
      },
      "cost": 1.5,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24,
      },
      "cost": 2.5,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24,
      },
      "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}


start_water_amt = resources["water"]
start_milk_amt = resources["milk"]
start_coffee_amt = resources["coffee"]
profit = 0


def is_transaction_successful(money_received, drink_cost):
  """returns True when the payment is accepted, or False if money is insufficient."""
  if money_received >= drink_cost:
      change = round(money_received - drink_cost, 2)
      print(f"Here is ${change} in change.")
      global profit
      profit += drink_cost
      return True
  else:
      print("Sorry that's not enough money. Money refunded.")
      return False


def add_coins():
  """Takes the user input and returns the total of all coins inserted"""
  print("Please insert coins.")

  quarters_amount = float(input("How many quarters?: ")) * 0.25
  dimes_amount = float(input("How many dimes?: ")) * 0.10
  nickels_amount = float(input("How many nickels?: ")) * 0.05
  pennies_amount = float(input("How many pennies?: ")) * 0.01
  return quarters_amount + dimes_amount + nickels_amount + pennies_amount


def is_resource_sufficient(order_ingredient):
  is_enough = True
  for item in order_ingredient:
      if order_ingredient[item] >= resources[item]:
          print(f"Sorry, there is not enough {item}.")
          is_enough = False
  return is_enough


def make_coffee(drink_name, order_ingredients):
  """Deduct the required ingredients from the resources"""
  for item in order_ingredients:
      resources[item] -= order_ingredients[item]
  print(f"Here is your {drink_name} ☕")


finished = False
while not finished:
  user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if user_input == "off":
      finished = True
  elif user_input == "report":
      print(f"Water: {start_water_amt}ml")
      print(f"Milk: {start_milk_amt}ml")
      print(f"Coffee: {start_coffee_amt}g")
      print(f"Money: ${profit}")
  else:
      drink = MENU[user_input]
      if is_resource_sufficient(drink["ingredients"]):
          payment = add_coins()
          if is_transaction_successful(payment, drink["cost"]):
              make_coffee(user_input, drink["ingredients"])
