print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You are tall enough to ride this rollercoaster!")
  age = int(input("How old are you? "))
  if age < 12:
    print("You have to pay $5")
  elif age > 18:
    print("You have to pay $12")
  else:
    print("You have to pay $7")
else:
  print("You are not tall enough to ride this rollercoaster!")