# This the lab 6 assignment
"""
Program that checks if 2 strings are equal or not.

I tried to create an advanced program that take into consideration
uppercases, lowercases,white spaces and long strings with different words
"""

# First step : get user inputs
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Second step: curate and lowercase
# It's important to le convert strings to lowercases and remove white spaces
# To do a proper comparison and avoid mistakes
# Better and clear code for future use
string1 = (str1.lower()).strip()
string2 = (str2.lower()).strip()

#Comparison with conditions
if string1 == string2:
    print("The strings are the same.")

# Nested conditions
elif string1 != string2:

    # Extra comparison with length method
    if len(string1) == len(string2):
        print("The strings are different but have the same length")

    else:
        print("The strings are different.")