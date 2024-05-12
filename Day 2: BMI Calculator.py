# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

BMI = float(weight) / (float(height) * float(height))

print(int(BMI))
