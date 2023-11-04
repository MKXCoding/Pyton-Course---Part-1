make = "Saab"
model = "9-5"
model_type = "Aero"
# output - Saab 9-5 "Aero"
car = make + ' ' + model + ' "' + model_type + '"'
print(car)
# f-string
car = f'{make} {model} "{model_type}"'
print(car)
