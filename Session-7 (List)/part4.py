numList = [1,5,10,19,32,-28]
numChecked = int(input("Enter a number to check: "))
count = 0
while True: 
    count += 1
    if count == 4:
        break
    elif numChecked in numList:
        numIndex = numList.index()
        print("Found, position " + str(numIndex))
    else:
        print("Not found in our list")

sum(numList,0)
print("Sum of all numbers is: ")
firstSum = 0
for i in numList:
    firstSum += i
print("Sum of all numbers is: ")

Num = input("Enter numbers seperated by space each: ")
listNum = Num.split(" ")
print("Sum of the list is: " + str(sum(listNum)))
evenList = []
for n in numList:
    if n % 2 == 0:
        evenList.append(n)
print("All even numbers are: ", end =" ")
print(*evenList, sep = ", ")

userEntered = input("Enter a list of number seperated by ,: ")
userList = userEntered.split(", ")
for k in userList:
    if int(k) % 2 == 0:
        print(k, end=" ")

