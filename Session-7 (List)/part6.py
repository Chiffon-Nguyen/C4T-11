scoreList = [45, 67, 56, 78, 99]
newScore = int(input("Enter new score: "))
scoreList.append(newScore)
sortedList = sorted(scoreList, key=int, reverse=True)
fiveHighest = sortedList[0:5]
for index, items in enumerate(fiveHighest):
    print(index + 1, items)