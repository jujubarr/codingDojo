'''
Assignment: Type List

Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
Your program input will always be a list. For each item in the list, test its data type. 

If the item is a string, concatenate it onto a new string. 

If it is a number, add it to a running sum. 

At the end of your program print the string, the number and an analysis of what the array contains. 

If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
'''

def printList(input):
    sum = 0
    stringConcat = ""
    listType = ""

    for elem in input:
        if int == type(elem):
            sum += elem
            listType = "int"
        elif str == type(elem):
            stringConcat += elem
            listType = "string"
            
    if (len(stringConcat) != 0) & (sum != 0):
        listType = "mixed"

    print sum
    print stringConcat
    print listType
    print "\n"

printList([1, 10, "cat", "dog", 100])
printList([1,2,3,4,5,6])
printList(["a", "b", "c", "dd"])
