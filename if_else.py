is_full = False
is_empty = True

if is_full:
    print("You're good to go!")
elif is_empty:
    print("You should refuel before You go!")
else:
    print("You're good to go, but You might refuel later")
print("Have a nice journey!")

"""
Exercise - write an if statement, that checks, if customer is a new client. If it is, he has to pay 
a deposit - 5% of the car value (car value is 10'000Eur). Create a variable, that states, that customer is new client 
and make calculation how much deposit he has to pay. Use f string to show a message - "You are new customer, You are 
obligated to pay XXX Eur deposit"
If not customer is returning client, he doesn't have to pay any deposit. In any case, user must see 
a message - "Enjoy Your trip"
"""


# Solution:

car_value = 10000
new_customer = True

if new_customer:
    deposit = car_value * 0.05
    print(f"You are new customer, You are obligated to pay {deposit}Eur deposit")
else:
    print("You don't have to pay deposit")
print("Enjoy Your trip!")
