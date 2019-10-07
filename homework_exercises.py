"""
1st,
Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
example user input of Python:
Would return" onononon (edited)
"""

print("Exercise #1 COMPLETE")
ex_string = "Python"
print(ex_string)

def last_two(n):
  new_string = ""
  i = 0
  while i < n:
    new_string = new_string + ex_string[-2:]
    i += 1
  return new_string

print(last_two(4))

"""
2nd,
Write a Python program to reverse a string
Example Python:
would return: nohtyP (edited)
"""

print("")
print("Exercise #2 COMPLETE")
ex_string = "Python"
print(ex_string)
new_string = ""
for i in ex_string:
  new_string = i + new_string
print(new_string)

"""
3rd
Write a Python program to reverse words in a string.
Example The big dog,
would return: dog big The
"""

print("")
print("Exercise #3 COMPLETE")
ex_string = "The big dog"
print(ex_string)
new_string_list = ex_string.split()
print(new_string_list)
new_string = ""
for i in new_string_list:
  new_string = i + " " + new_string
print(new_string.strip())

"""
4th
Write a Python program to calculate the length of a string
Example: "apple"
The print out should be: 5
"""

print("")
print("Exercise #4 COMPLETE")
ex_string = "apple"
print(ex_string)
print(len(ex_string))


"""
5th
Write a Python program to get a single string from two given strings
Example.
string1 = "the"
string2 = "dog"
Would be printed as: "the dog" (edited)
"""
print("")
print("Exercise #5 COMPLETE")
ex_string = "the"
ex_string_two = "dog"
print(ex_string)
print(ex_string_two)
new_string = ex_string + " " + ex_string_two
print(new_string)


"""
6th
Write a Python program to change a given string to a new string where the first and last chars have been exchanged
Example: "the dog"
Would print out "ghe dot"
"""

print("")
print("Exercise #6 COMPLETE")
ex_string = "the dog"
print(ex_string)
j = len(ex_string) - 1
new_string = ex_string[-1:] + ex_string[1:j] + ex_string[:1]
print(new_string)

