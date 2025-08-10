# This the lab 3 assignment
"""
Write a program to check how many days there are in 2023 by using the string function.
"""
#import library
from datetime import datetime, timedelta


#uses strings input to convert into dates following a specific format
firstDayIn2023 = datetime.strptime("2023-01-01", "%Y-%m-%d")
lastDayIn2023 = datetime.strptime('2023-12-31', "%Y-%m-%d")


#substract to get the exact days number of year 2023.
# we have to add one to the days number because last day was excluded
daysOf2023 = (lastDayIn2023 - firstDayIn2023).days + 1

#output a personalized result with days only.
print('Total days of year 2023 were:', daysOf2023, 'days')
#we can also convert days to str
print('Total days of year 2023 were: ' + str(daysOf2023) + ' days')
