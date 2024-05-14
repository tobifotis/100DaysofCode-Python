target = int(input()) # Enter a number

# Your code here
target = target + 1

sum = 0
for item in range(0, target):
  if item % 2 == 0:
    sum = sum + item

print(sum)

