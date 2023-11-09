good_income = False
good_credit = False
has_credits = True

if good_credit and good_income and not has_credits:
    print("You can get credit for a new car or second-hand car")
elif good_income or good_credit or not has_credits:
    print("You can get credit only for a second-hand car")
else:
    print("Sorry, You are not entitled for any credit")
