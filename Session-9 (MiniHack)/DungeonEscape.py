import random
matrix_row = int(input("Enter a number of row: "))
matrix_col = int(input("Enter a number of row: "))
key = {
    'x': random.randint(1,matrix_row + 1),
    'y': random.randint(1,matrix_col + 1)
}
escape = {
    'x': random.randint(1,matrix_row + 1),
    'y': random.randint(1,matrix_col + 1)
}
player = {
    'x': random.randint(1,matrix_row + 1),
    'y': random.randint(1,matrix_col + 1)
}
hasKey = False
while True:
    for y in range(1,matrix_col + 1):
        for x in range (1,matrix_row + 1):
            if player['x'] == x and player ['y'] == y:
                print("P", end = " ")
            elif key['x'] == x and key['y'] == y:
                print("K", end = " ")
            elif escape['x'] == x and escape['y'] == y:
                print("E", end = " ")
            else:
                print("-", end = " ")
        print("")
    if player['x'] == key['x'] and player['y'] == key['y']:
        hasKey = True
        key['x'] = matrix_row + 2
        print("You've got the key")
    if player['x'] == escape['x'] and player['x'] == escape['x']:
        if hasKey == True:
            print("You escape!")
            break
    UserInput = input("Your move? (W,A,S,D): \n") 
    if player['x'] in range (1,matrix_row + 1) and player['y'] in range (1,matrix_col + 1):
        if UserInput.upper() == 'W':
            if player['y'] == 1:
                print("You reach the wall")
            elif hasKey == False: 
                print("You can't escape without key")
            else:
                player['y']-=1
        elif UserInput.upper() == 'S':
            if player['y'] == matrix_col:
                print("You reach the wall")
            elif hasKey == False: 
                print("You can't escape without key")
            else:
                player['y']+=1
        elif UserInput.upper() == 'A':
            if player['x'] == 1:
                print("You reach the wall")
            elif hasKey == False: 
                print("You can't escape without key")
            else:
                player['x']-=1
        elif UserInput.upper() == 'D':
            if player['x'] == matrix_col:
                print("You reach the wall")
            elif hasKey == False: 
                print("You can't escape without key")
            else:
                player['x']+=1
        else: 
            print("Not a right move")


