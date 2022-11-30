#This is a list in python
'''
List's value can be changed, but ARRAY's VALUE CANNOT BE CHANGED.
'''
names = {"Harry", "Ron", "Hermione"}
print(names)
print(names[0])

#How to add new name to the list
#Append means: Add to(The VERY END, VERY LAST ONE)
'''
This will add Drace to {"Harry", "Ron", "Hermione"}
so it become {"Harry", "Ron", "Hermione","Drace}
'''

names.append("Drace")

#How to sort the list
names.sort()

#How to print the updated list
print(names)