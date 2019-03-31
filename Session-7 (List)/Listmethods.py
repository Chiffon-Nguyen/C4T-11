someList = ["some", "thing","should","be","here" ] 
anotherList = [0,1,4,9,16,25,49]
someList.append("right?") #add element to the end of the list
print(someList)
anotherList.insert(6,36) #add element to a given index
print(anotherList)
try:
    someList.index("yay")
except ValueError:
    print("Value Error occur")
finally:
    print("Ignore error, it'll run no matter what")
someList.remove("right?")
print(someList)
anotherList.pop(7) #delete the element in its index and return it to the screen
anotherList.reverse()
print(anotherList)
someList.extend(anotherList) #extend by another list you enter
print(someList)




