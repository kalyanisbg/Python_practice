# ask the user for the temperature
temp = int(input("What is the temperature?"))
# evaluate if the temp, is less than 0
if temp<0:
    print(f"The temperature is {temp}")
# print if the input is less than 0

# use string formatting to adjust your output


# 'it is freezing: TRUE'

### EXERCISE 1 ###
"""
You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

Input the price of a burger using input()
Check whether the price is less than or equal (<=) 10.00
Print the result in the format below
Burger is within budget: True

Hint: remember to convert the input from a string to a decimal with float()

"""
#Input the price of a burger using input()
price = float(input("Please input the price of the burger (no currency, please)"))
condition = price<=10.00
#Check whether the price is less than or equal (<=) 10.00
if condition:
    print(f"Burger is within budget: {condition}")

#Print the result in the format below
#Burger is within budget: True



