# This the lab 7 assignment
"""
Create a tuple and access its elements
"""

## Access element from a tuples
# tuple1 = (1, -2, 'Hello', [1, 2, 3], (-5, -6, 'H'))

# print(tuple1[1]) #should show -2 as it is the  index 1 - note that indexes start from 0
# print(tuple1[2]) #Should show the string 'Hello'
# print(tuple1[2][0]) #String are indexed as well, should show the letter H of string Hello
# print(tuple1[2][4]) #should show the letter o of string Hello
# print(tuple1[3][2]) #Works on nested list inside the tuple
# print(tuple1[4][2]) #Works on nested tuples and lists

## Yes, tuples allow negative indexing
# print(tuple1[-1])  #should show the last element
# print(tuple1[-2])  #should show the element before the last one
# print(tuple1[-2][-2]) #access nested element using negative indexing works as well


tuple1 = (1, -2, 'Hello', [1, 2, 3], (-5, -6, 'H'))
## How to delete tuples elements.
## Tuples are immutable, so we can't delete elements individually but we can remove the entire tuples
# example
tuple1[0] = 5 # Will output an error
del tuple1    # will delete tuple from the memory
print(tuple1) # Name error will be shown since tuples1 was completely deleted

#we can also delete whole tuples nested in a list by using the list method pop()
list1 = [1,2, (3, 5)]
print(list1.pop(2))  #pop index 2 which will remove the nested tuples
print(list1)