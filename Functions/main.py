import numpy
import datetime

### EXERCISE 1 ###

"""

You have friends at your house for dinner and you've accidentally burnt the lasagne. Time to order pizza.

Write a program calculate how many pizzas you need to feed you and your friends

"""

# number_of_people = input("How many of you are around?")
# number_of_slices = float(input("How many slices are you gonna have? xxx"))
# pizza_number = number_of_slices * number_of_people
# print("You need  {} pizza(s)")

### EXERCISE 2 ###

"""

Write a program that issues notifications to drivers about PCN (Penalty Charge Notice) for £130. 

If a person pays within 14 days, then the amount will be reduced to £65.
"""

# start_time = datetime.time()
# end_time = datetime.time()
# time_diff = datetime.timedelta(start_time, end_time)

# Get the PCN issue date
# pcn_date = input("Please enter the PCN issue date in the following format DDMMYYYY")
# pcn_date = datetime.strptime(pcn_date, "%d %b %Y")

# Work out 14 days later
#deadline = datetime.timedelta(days=14)
#deadline = datetime.date(deadline)
#print(deadline.type)

# Format that date & display it

x = 67
print(x.type())

def one_to_twenty():
    x=[]
    for i in range(1, 21):
        x.append(i)
    print(x)
    return x
    

