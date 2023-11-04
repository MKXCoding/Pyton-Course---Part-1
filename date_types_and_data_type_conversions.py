# Option 1
year_of_manufacture = int(input("First registration year: "))
age = 2023 - year_of_manufacture  # Behind the scenes - 2023 - "2014" - one is int, other is str
print(type(year_of_manufacture))
print(age)

# Option 2:
year_of_manufacture = int(input("First registration year: "))
age = 2023 - year_of_manufacture  # Behind the scenes - 2023 - "2014" - one is int, other is str
print(age)

# Excercise - make an input that asks weight of the car in lb and convert them to kgs

# Solution
weight_lbs = input("Weight in lbs: ")
weight_kgs = str(int(weight_lbs) * 0.4536)
print("Car weight is kgs: " + weight_kgs)
