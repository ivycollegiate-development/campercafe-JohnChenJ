#This is a list in python
'''
List's value can be changed, but ARRAY's VALUE CANNOT BE CHANGED.
'''
names = ["Harry", "Ron", "Hermione"]
#IMPORTANT!list use [], {} is for class and methods!
#How to print the ENTIRE list
print(names)
#How to print the FIRST item in the list
print(names[0])

#How to add new name to the list
names.append("Draco")
#Append means: Add to(The VERY END, VERY LAST ONE)
'''
This will add Drace to {"Harry", "Ron", "Hermione"}
so it become {"Harry", "Ron", "Hermione","Draco"}
'''

#How to sort the list
names.sort()

#How to print the updated list?
#The list is already mutated so you can just do it by print the list again.
print(names)
'''
As you can see, 'sort' sort names based on Ascii code.
'''