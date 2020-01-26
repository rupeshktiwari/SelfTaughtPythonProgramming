#**********Lambda function********

#program to find the square the number

square = lambda n:n*n
print('square of the number is :',square(2))

#program to find the sum of the number
sum = lambda a,b :a+b
print('sum of the numbers is',sum(5,10))

#function to find the largest of the numbers
s = lambda a,b:a if a>b else b
print('largets of two numbers 10,20 is',s(10,20))


#*******filter function*********

# list with even and odd numbers
def isEven(x):
    if x%2==0:
        return True
    else :
        return False
l=[1,3,2,23,33,22,24,46]
l1=list(filter(isEven,l))
print(l1)

l2 =[1,2,3,4,5,6,7,8,9]
EL = list(filter(lambda x:x%2==0,l2))
print(EL)
OD=list(filter(lambda x:x%2!=0,l2))
print(OD)

#********Map function**********
#program to double the list elements using map function
l=[1,2,3,4,5,6]
l1=list(map(lambda x:x*2,l))
print(l1)

#program to find square of the list item

l=[2,3,4,5,6,7,8,9]
l1=list(map(lambda x:x*x,l))
print(l1)

#*******reduce function*********
#reduce function reduce the sequence of elements into single elementbby applying the specified function.
from functools import*
l=[1,2,3,4,5,6,7,8,9]
result =reduce(lambda x,y:x+y,l)
print(result)

