import random
import time
count = 0 #put it into while loop will reset it
while True:
    a = random.randint(-30,30)
    b = random.randint(-30,30)
    c = a + b
    d = random.randint (-3,3)
    c = c + d
    print (f" {a} + {b} = {c}")
    solution = int(input("True: 1 or False: 2 "))
    if d == 0:
        c = True
        if solution == 1:
            print("You're right")
            count += 1
            print("Points: " + str(count))
        else: 
            print("You're false. Game over")
            print("You have " + str(count) + " correct answers")
            break
    else: 
        c = False
        if solution == 2:
            print("You're right")
            count += 1
            print("Points: " + str(count))
        else: 
            print("You're false. Game over")
            print("You have " + str(count) + " correct answers")
            break

