colorList = ['magenta', 'teal', 'maroon']
print("Our color list is: ")
print(*colorList)

newColor = str(input("Enter a new color: "))
colorList.append(newColor)
anotherColor = str(input("Enter a new color: "))
while True:
    anotherIndex = int(input("Enter its index between 1 and 4: "))
    if anotherIndex < 3 and anotherIndex >=0:
        break
    else:
        continue
colorList.insert(anotherIndex - 1, anotherColor)
print(*colorList)

while True:
    delItems = input("Enter an index or items to delete: ")
    if colorList == []:
        print("This list is empty")
        break
    elif delItems.isdigit() and int(delItems) <= len(colorList):
        colorList.pop(int(delItems) - 1)
        for index, items in enumerate(colorList):
            print(index + 1, items)
    else:
        if delItems in colorList:
            colorList.remove(delItems)
            for index, items in enumerate(colorList):
                print(index + 1, items)
        else: 
            print("There's no such an item")

#draw a line with 3 colors
from turtle import *
colorList = ['magenta', 'teal', 'maroon']

for color in colorList:
    pencolor(color)
    forward(80)

mainloop()

