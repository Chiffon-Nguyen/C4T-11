#Set: no duplicates, no 
A = {2,3,4,5,6}
B = {0,1,2,3} 
C = A & B # & = items exist in both set
print(C)
D = A | B # | = items in either set A or set B
print(D)
E = A - B
print(E) # - = items in set A but not set B

#Lambda
nums = {1,1,3,5,7,2,2,4}
numFilter = filter(lambda x: x > 1, nums)
a = (lambda x: x * (x+1)) (6) #<lambda>(x)
print(a)

#Recursion
def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
print(power(7,3))

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)
print(fibonacci(10))
