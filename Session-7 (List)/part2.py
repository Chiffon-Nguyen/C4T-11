favsList = ['coding','reading','music','cats']
while True:
    Input = input("Enter C, R, U or D: ").upper()
    if Input == 'C':
        favorite = str(input("Enter your favorite thing: "))
        favsList.append(favorite)
    if Input == 'R':
        if favsList == []:
            print("There's nothing in this list")
        else:
            print(*favsList, sep = '\n')
    if Input == 'U':
        print("List Update")
        indexEntered = int(input("Enter an index between 0 and 3: "))
        stringEntered = str(input("Enter an element: "))
        favsList[indexEntered + 1] = stringEntered
    if Input == 'D':
        print("List Update")
        IndexEntered = int(input("Enter an index between 0 and 4: "))
        favsList.pop(IndexEntered)

    
    
