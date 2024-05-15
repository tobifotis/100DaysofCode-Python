# Ask user for input
user_num = int(input("Enter the number: "))
for each_number in range(1, 13):
    mul = user_num * each_number
    print(f"{user_num} x {each_number} = {mul}")