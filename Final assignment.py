def find_max(inputList):
    a = int(inputList[0])

    try:
        for x in range(1,len(inputList)):
            if a<inputList[x]:
                a = inputList[x]

        return a

    except ValueError:
        print("Error: Please enter only numbers.")

    except IndexError:
        print("Error: The list is empty.")

# let's use the user's number inputs and convert them to integers since input are considered string
# we can use split method to separate numbers with a comma.
try:
    userInput = input('Enter a list of numbers separated by comma: ')
    #we can use a compact way to loop through the list and convert all items to numbers
    numbers = [int(num) for num in userInput.split(',')]
    print('The highest number of your list is:',find_max(numbers))
except ValueError:
    print("Error: Please enter only numbers.")

#example 5,32,123,-23
#output => The highest number of your list is: 123

