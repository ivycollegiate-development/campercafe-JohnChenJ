# This is how you create an empty set
s = set()

#And this is how you add elements to the set:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(1)

'''
What are elements? Think of it as every unit of index contained within set
'''

#Now print the set
#List vs array vs set
'''
List&Array very well for temporary database that need to be in there.
Set are better for permanent.
Set will not repeat value that you added in, even though it is changeable
So as a result, it will only print {1, 2 ,3 ,4}
'''
print(s)

s.remove(2)

#What will happen?
print(s)
#It will remove that specific number

#Weakness of user interface: Do thing for you automatically