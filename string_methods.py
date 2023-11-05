message = "welcome to Python course"
print(len(message))  # function to return length of items - can be on string, list etc
print(message.upper())  # method to convert message to uppercase, lowercase etc
print(message.lower())
print(message.capitalize())
print(message.find("e"))  # Returns index of first occurrence or -1
print(message.replace("Python", "JavaScript"))
print(message.replace("o", "a"))
print('Python' in message)  # Returns boolean value

# More advanced methods:
# Checking if all characters in the string are alphanumeric (a combination of alphabets and numbers)
print(message.isalnum())  # Returns False because there are spaces
# Splitting the string into a list of substrings based on a delimiter (default delimiter is any whitespace)
print(message.split())  # Splits the message on spaces and returns a list of words
# Counting how many times a substring appears in the string
print(message.count('o'))  # Outputs the number of times 'o' appears in the message

# String formatting using `format()`
print("Hello, {}. You are currently on a {} course.".format("Alice", "Python"))

# Exercise - Create a "Hello, Alice. You are currently on a PYTHON course." string
# with these variables and 'format' method:
name = "mars"
course = "Python"

# Solution
print("Hello, {}. You are currently on a {} course.".format(name.capitalize(), course.upper()))
print(f"hello, {name.capitalize()}. You are currently on a {course.upper()} course.")
