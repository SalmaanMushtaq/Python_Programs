import random

# 🚨 Don't change the code below 👇
"""test_seed = int(input("Create a seed number: "))
random.seed(test_seed)"""

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#This code does the same thing as the code below this code.
"""name_length = len(names)
random_choice = random.randint(0, name_length-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")"""

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")