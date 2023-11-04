greeting = "It's me!"
print(greeting)
greeting_2 = 'Hey, "Python"'
print(greeting_2)
# Long string:
long_string = """
Hello, Customer
Thanks for Your purchase!

Greetings, Mars
"""
print(long_string)

indexing_string = "Multiple word string for indexing"
print(indexing_string[0])
print(indexing_string[-2])
print(indexing_string[:8])
print(indexing_string[8:])
print(indexing_string[:])

# Exercise - what code we have to write to get this output - Nl?
netherlands = "Netherlands"
# Solution 1 (not 100% correct):
letter_1 = netherlands[0]
letter_2 = netherlands[6]
print(letter_1, letter_2)
# Solution 2:
netherlands = "Netherlands"
letter_1 = netherlands[0]
letter_2 = netherlands[6]
print(letter_1 + letter_2)
# Solution 3:
netherlands = "Netherlands"
letter_1 = netherlands[0]
letter_2 = netherlands[6]
print(letter_1, letter_2, sep='')
