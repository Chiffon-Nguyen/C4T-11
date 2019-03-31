listDist = ["ST", "BD", "BTL", "CG", "ĐĐ","HBT"]
listPol = [150300,247100,333300,266800,420900,318000]
sortedlistDict = sorted(listPol,key=int)
min = sortedlistDict[0]
revlistDict = sorted(listPol, key = int, reverse = True)
max = revlistDict[0]
minIndex = int(listPol.index(min))
maxIndex = int(listPol.index(max))
print("Most populated district: " + str(listDist[maxIndex]))
print("Least populated district: " + str(listDist[minIndex]))
