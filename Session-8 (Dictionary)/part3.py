favBook = {
    "name" : "Always and Forever, Lara Jean",
    "publish year": 2017,
    "author": "Jenny Han",
    "main chars": ["Lara Jean Song Covey", "Peter Kavinsky"],
    "description": "growth pathway into uni of LJ"
}
favBook["publisher"] = "HapperCollins"

for k, v in favBook.items():
    print(k, "-", v, '\n')

favBook["main chars"] = ["Ravi", "Margot Song Covey"]
newChars = ["Lara Jean Song Covey", "Peter Kavinsky"]
favBook["main chars"].extend(newChars)
favBook["main chars"].pop(0)
print(favBook["main chars"][1])
for mchar in favBook["main chars"]:
    print(mchar)

for k, v in favBook.items():
    print(k,v)

#quiz

quiz1Opt = {
    "A": "I still love you",
    "B": "All the boys I loved",
    "C": "Always and Forever Love you",
    "D": "The summer I turned pretty"
}
print("Which is the name of a Jenny's book?", '\n')
for k, v in quiz1Opt.items():
    print(k,v)
quiz1Ans = input("Enter your answer: ")
if quiz1Ans.upper() == "D":
    print("Correct answer")
else: 
    print("Not a correct answer")

quiz2Opt = {
    "A": ""
}
