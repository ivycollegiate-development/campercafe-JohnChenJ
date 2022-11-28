#num = input("Number: ")
num = int(input("Number:"))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")
#In Python, tab is very crucial, just like Java
#Anyway, put tab to organize your code
'''
To fix this, specify input as int
If you satisfy the first condition, it will not care about elif or else
The program will always consider the earilest condition satisfied

For example, if second elif condition is satisfied, third, fourth, or the 100th elif..., else will not be cared

In Java, you have to put: int a = 69;



In github, ONLY CREATOR can MERGE BRANCH
Other will submit codes by pull request(To separate everyone's branch from each other)

If you approve their request, you can merge your branch with their requested branch.
You can also check their mistake from their request.
'''