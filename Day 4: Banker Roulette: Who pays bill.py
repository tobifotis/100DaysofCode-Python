names = names_string.split(", ")

# get the total number of names in the list 
num_items = len(names)

# generate random numbers between 0 and last index.
import random
random_choice = random.randint(0, num_items - 1)

# Choose and print the random name
x = names[random_choice]
print(f"{x} is going to buy the meal today!")