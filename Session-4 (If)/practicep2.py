from random import randint
#p3
print(randint(0, 101))
#p4
n = randint(0, 101)
print(n)
if n < 30: 
    print("Rainy")
elif n in range (30,61):
    print ("Cloudy")
else:
    print ("Sunny")