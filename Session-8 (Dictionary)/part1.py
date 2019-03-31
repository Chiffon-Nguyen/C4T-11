# nullDict = {}
# drink = {
#     'favorite drink': 'bubble tea'
# }
# print(drink)
# foodnDrink = {
#     'fav drink': 'bubble tea',
#     'fav food': 'sushi'
# }
# print(foodnDrink)

favBook = {
    "name" : "Always and Forever, Lara Jean",
    "author": "Jenny Han",
    "description": "growth pathway into uni of LJ"
}

# print(favBook)
favBook["series"] = "To All the boys I loved before"
# print(favBook)
# keyInput = input("Enter another attribute you want to add: ")
# valueInput = input("Enter content for that attribute: ")
# favBook[keyInput] = valueInput
# print(favBook)

# print(favBook["name"])

# for k,v in favBook.items():
#     if k == "name" or k == "description":
#         print(k, v)

favBook["description"] += " LJ in her senior year, and has to decide where to go to the college."
favBook["description"] += " " + input("Enter further description: ")
print(favBook["description"])
del favBook["series"]
delInput = input("Enter a key you want to del: ")
if delInput in favBook.keys():
    del favBook[delInput]
print(favBook)




