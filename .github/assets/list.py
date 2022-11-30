#This is a list in python
'''
List's value can be changed, but ARRAY's VALUE CANNOT BE CHANGED.
'''
names = ["Harry", "Ron", "Hermione"]
#IMPORTANT!list use [], {} is for class!
print(names)
print(names[0])

#How to add new name to the list
#Append means: Add to(The VERY END, VERY LAST ONE)
'''
This will add Drace to {"Harry", "Ron", "Hermione"}
so it become {"Harry", "Ron", "Hermione","Draco}
'''

names.append("Draco")

#How to sort the list
names.sort()

#How to print the updated list
print(names)
'''
As you can see, 'sort' sort names based on Ascii code.
'''