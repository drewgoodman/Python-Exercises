# Dictionaries

# Write a Python script to add a key to a dictionary
# Write a Python script to concatenate following dictionaries to create a new one
# Sample Dictionary : 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# 3.Write a Python script to check if a given key already exists in a dictionary

dic1 = {
    1 : 10,
    2 : 20
}

dic2 = {
    3 : 30,
    4 : 40
}

dic3 = {
    5 : 50,
    6 : 60
}

dictionary_app = {
    3 : 5
}

dictionary_app.update({ 7 : 11})
print(dictionary_app)

dictionary_full = {}
dictionary_full.update (dic1)
dictionary_full.update (dic2)
dictionary_full.update (dic3)
print(dictionary_full)

if 5 in dictionary_full:
    print("The key 5 is in the full dictionary.")
else:
    print("The key 5 is NOT in the fully dictionary.")


# Tuples

# Write a Python program to create a tuple.
# Write a Python program to create a tuple with different data types.
# Write a Python program to create a tuple with numbers and print one item




# Strings

# 1.Write a Python program to calculate the length of a string
# 2. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

string_one = 'abc'
string_two = 'xyz'

print("The length of string 'abc' is " + str(len(string_one)))

string_joined = string_two[:2] + string_one[2:] + " " + string_one[:2] + string_two[2:]
print(string_joined)