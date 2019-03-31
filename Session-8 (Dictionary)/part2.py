# aboutMe = {
#     "name": "Chiffon",
#     "age": 17,
#     "education": "high school",
#     "hobby": "reading"
# }
# testInput = input("Enter a thing u want to know about me: ")
# if testInput in aboutMe: 
#     print(testInput, "exists in the dict")
#     print("My",testInput, "is", aboutMe[testInput])
# else:
#     print(testInput, "is not in the dict")

# abbr = {
#     "btw": "by the way",
#     "asap": "as soon as possible",
#     "fyi": "for your information",
#     "lmk": "let me know",
#     "j4f": "just for fun",
#     "lol": "laugh out loud"
# }

# while True:
#     checkDict = input("Do you want to check the dict? If yes, enter YES. If no, enter NO." + "\n")
#     if checkDict.upper() == "NO":
#         break
#     elif checkDict.upper() == "YES":
#         testAbbr = input("Enter a thing u want to know about abbreviation: ")
#         if testAbbr.lower() in abbr:
#             print(abbr[testAbbr])
#     else:
#         print("Key is not valid")
#         continue

# catering at a restaurant
Huy = {
    "name": "Huy",
    "role": "waiter",
    "hours": 12,
    "salary per hr ($)": 0.8
}
Tung = {
    "name": "Tung",
    "role": "cook",
    "hours": 24,
    "salary per hr ($)": 1.5
}
M_Duc = {
    "name": "M.Duc",
    "role": "manager",
    "hours": 20,
    "salary per hr ($)": 2.0
}
resEmployment = []
resEmployment.append(Huy)
resEmployment.append(Tung)
resEmployment.append(M_Duc)

Don = {
    "name": "Don",
    "role": "waiter",
    "hours": 12,
    "salary per hr ($)": 0.9
}
H_Duc = {
    "name": "H.Duc",
    "role": "waiter",
    "hours": 14,
    "salary per hr ($)": 0.7 
}
resEmployment.append(Don)
resEmployment.append(H_Duc)
print(resEmployment[2], '\n')
resEmployment.pop(-1)
payment = 0
for employee in resEmployment:
    print(employee, sep = '\n')
    earning = employee["hours"] * employee["salary per hr ($)"]
    payment += earning
    print(employee["name"], "earns",earning)
print("They have to pay", int(payment), "dollars in total")


