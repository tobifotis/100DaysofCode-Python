print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

names_combined = name1 + name2
lower_names = names_combined.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = str(first_digit) + str(second_digit)
score2 = int(score)

if score2 < 10 or score2 >90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score2 >= 40 and score2 <=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


