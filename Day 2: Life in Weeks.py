print('Welcome to the "Weeks left Alive" Calculator!')

name = input("What is your name? ")

age = int(input(f"\nHello, {name}. How old are you? "))

x = (90 - age) * 52

print(f"\nYou have {x} weeks left.")
