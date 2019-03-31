nullList = []
favList = ['coding']
favsList = ['coding','reading','music','cats']
favsList.append('cute things')

favsList.append(input("Enter another thing you like: "))
print(*favsList)

print(*favsList, sep=', ') #sep = separator
print(*favsList, sep=' | ') #sep = separator

print(favsList[0], favsList[-1], favsList[-2])
print(favsList[0].upper(), favsList[-1].upper(), favsList[-2].upper())

print(favsList)

favsList[0] = 'The fault in our stars'
print(favsList[0])
favsList[-1] = 'Leah on the offbeat'

indexEntered = int(input("Enter the index between 0 and 3"))
stringEntered = str(input("Enter the element"))
favsList[indexEntered] = stringEntered

favsList.pop(1) #remove element in numbder #2

try:
    favsList.remove('LOL')
except ValueError:
    print("There's no such an element")

favsList.pop(int(input("Enter an index to remove its element")))

try:
    favsList.remove(input("Enter an element to remove"))
except ValueError:
    print("There's no such an element")

print(*favsList, sep = '\n') #print list items in seperated lines

#print uppercased list items in seperated lines
for x in favsList: 
    print(x.upper(), sep = '\n') 

#print list items with its index
count = 1
for x in favsList: 
    print(str(count) + ". " + x.upper()) 
    count += 1

#print list items with its index
for index, items in enumerate(favsList):
    print(index + 1, items)

#check if elements in the list contain something
for x in favsList:
    if 'e' in x or 'E' in x:
        print(x)





